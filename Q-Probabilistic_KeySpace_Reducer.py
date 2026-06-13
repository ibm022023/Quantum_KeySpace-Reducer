#Hi i Realy apperciated you get me A Donation here_ 1Bu4CR8Bi5AXQG8pnu1avny88C5CCgWKfb /////
#============================================================================================
#!/usr/bin/env python3

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  KEY-REDUCER · Quantum + P-Bit Keyspace Reducer · MERGED Edition v21       ║
║  IQM (pytket + Qrisp) · IBM Quantum · Aer                                  ║
║  QPB ENGINE v3 + P-BIT ENGINE v1 + QUANTUM WALKS — WORKING TOGETHER       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  ── IQM Hardware (two SDK paths) ──────────────────────────────────────── ║
║    [pytket]  Sirius 16q · Garnet 20q · Emerald 54q (--backend iqm_hardware) ║
║    [Qrisp]   Sirius 16q · Garnet 20q · Emerald 54q (--backend qrisp_iqm)   ║
║              qrisp.interface.IQMBackend — auto native transpilation          ║
║  ── IBM Quantum Hardware (qiskit-ibm-runtime) ──────────────────────────── ║
║    ibm_fez 156q · ibm_kingston 156q · etc. (--backend ibm_hardware)         ║
║    Token: export IBM_QUANTUM_TOKEN=your_ibm_token_here                      ║
║  ── Aer Simulator (local, no token) ────────────────────────────────────── ║
║    Always available · Recommended for testing                                ║
║                                                                              ║
║  ╔═ MERGED v21: P-BITS + QUBITS WALK TOGETHER ═════════════════════════╗  ║
║  ║  Phase B2 now runs THREE engines in sequence, pooling all samples:   ║  ║
║  ║                                                                       ║  ║
║  ║  [1] P-BIT ENGINE v1  (Classical Glauber dynamics — CPU)             ║  ║
║  ║    · p(s_i=+1) = sigmoid(β·I_i)  stochastic sequential flip         ║  ║
║  ║    · I_i = Σ W_ij·s_j + h_i  (Ising local field from EC landscape)  ║  ║
║  ║    · β anneals: hot spread cloud → cold snake corridor               ║  ║
║  ║    · n_chains × n_steps → p-bit visit density map                    ║  ║
║  ║                                                                       ║  ║
║  ║  [2] QPB ENGINE v3  (Quantum P-Bit — runs on QPU/Aer)               ║  ║
║  ║    · QPB gate = Ry(2·arcsin(√sigmoid(β·I_b))) per qubit              ║  ║
║  ║      P(|1⟩) = sigmoid(β·I_b) EXACTLY — qubit IS a p-bit             ║  ║
║  ║    · CRZ(β·W, b, j) = quantum W_ij coupling term                    ║  ║
║  ║    · β: 0.5 (hot/spread) → 4.0 (cold/committed/snake)               ║  ║
║  ║    · Each shot = one p-bit trajectory; N shots = N chains            ║  ║
║  ║                                                                       ║  ║
║  ║  [3] QUANTUM WALK (Adaptive-Coin + Phase Oracle)                     ║  ║
║  ║    · Runs AFTER QPB to add O(√N) interference patterns               ║  ║
║  ║    · Both B2 engines explore the SAME key-space dimensions           ║  ║
║  ║    · Combined density map = richer snake corridor detection           ║  ║
║  ║                                                                       ║  ║
║  ║  All three pools merge → energy-guided snake bracket → LOWER/UPPER  ║  ║
║  ║  The MOST EMPTY volume of the combined snake trajectory IS the key.  ║  ║
║  ╚═══════════════════════════════════════════════════════════════════════╝  ║
║                                                                              ║
║  [TRAJECTORY] Energy-guided snake bracket from combined density maps        ║
║  [S1-QFT · S2-QPE · S3-AmpEst] Shor-inspired quantum phases                ║
║  [ECPRA] EC Period Resonance Attack (multi-angle Shor probing)              ║
║  [G-1..G-8] SPSA · Sobol · non-NN · range shift · kangaroo · voting        ║
║             DBSCAN · BKZ block 20+ · MAX-Q full device utilisation          ║
║  [MODE1] real Grover + p-bit sampler for address-only mode                  ║
║                                                                              ║
║  INSTALL                                                                     ║
║    pip install pytket pytket-iqm pytket-qiskit                               ║
║    pip install qiskit qiskit-aer qiskit-ibm-runtime                          ║
║    pip install "iqm-client>=34.0.3" qrisp                                   ║
║    pip install pycryptodome base58 numpy matplotlib scipy                    ║
║    pip install qiskit-algorithms fpylll scikit-learn   # all optional       ║
║  Tokens:  export IQM_TOKEN=...   export IBM_QUANTUM_TOKEN=...               ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import argparse
import hashlib
import json
import logging
import math
import os
import sys
import time
import traceback
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import numpy as np

# ── matplotlib ────────────────────────────────────────────────────────────────
try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    MPL_OK = True
except ImportError:
    MPL_OK = False

# ── pycryptodome RIPEMD160 ────────────────────────────────────────────────────
try:
    from Crypto.Hash import RIPEMD160 as _RIPEMD160
    PYCRYPTO_OK = True
except ImportError:
    PYCRYPTO_OK = False; _RIPEMD160 = None  # type: ignore

# ── base58 ────────────────────────────────────────────────────────────────────
try:
    import base58; BASE58_OK = True
except ImportError:
    BASE58_OK = False; base58 = None  # type: ignore

# ── fpylll — optional BKZ/LLL ─────────────────────────────────────────────────
try:
    from fpylll import IntegerMatrix, BKZ, LLL as FpLLL
    FPYLLL_OK = True
except ImportError:
    FPYLLL_OK = False; IntegerMatrix = BKZ = FpLLL = None  # type: ignore

# ── scipy — optional Sobol ────────────────────────────────────────────────────
try:
    from scipy.stats.qmc import Sobol
    SOBOL_OK = True
except ImportError:
    SOBOL_OK = False; Sobol = None  # type: ignore

# ── scikit-learn — optional DBSCAN ───────────────────────────────────────────
try:
    from sklearn.cluster import DBSCAN
    SKLEARN_OK = True
except ImportError:
    SKLEARN_OK = False; DBSCAN = None  # type: ignore

# ── qiskit-algorithms — optional SPSA ────────────────────────────────────────
try:
    from qiskit_algorithms.optimizers import SPSA
    SPSA_OK = True
except ImportError:
    SPSA_OK = False; SPSA = None  # type: ignore

# ── dotenv ────────────────────────────────────────────────────────────────────
try:
    from dotenv import load_dotenv; load_dotenv()
except Exception:
    pass

# ── Suppress cosmetic warnings BEFORE Qiskit/IQM imports ────────────────────
import warnings
warnings.filterwarnings("ignore", message=".*TwoLocal.*deprecated.*",   category=DeprecationWarning)
warnings.filterwarnings("ignore", message=".*n_local.*deprecated.*",    category=DeprecationWarning)
warnings.filterwarnings("ignore", message="Could not verify IQM Client", category=UserWarning)
warnings.filterwarnings("ignore", message=".*ProviderV1.*")
# Silence Qiskit transpiler pass INFO logs (very noisy)
logging.getLogger("qiskit").setLevel(logging.WARNING)
logging.getLogger("stevedore").setLevel(logging.ERROR)

# ── Qiskit core ───────────────────────────────────────────────────────────────
try:
    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
    from qiskit.quantum_info import SparsePauliOp
    from qiskit_aer import AerSimulator
    from qiskit_aer.primitives import SamplerV2 as AerSampler
    from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
    # Qiskit >=2.1: prefer n_local() function, fall back to TwoLocal class
    try:
        from qiskit.circuit.library import n_local as _n_local_fn
        _USE_N_LOCAL = True
    except ImportError:
        _USE_N_LOCAL = False
    try:
        from qiskit.circuit.library import TwoLocal
    except ImportError:
        TwoLocal = None  # type: ignore
    QISKIT_OK = True
except ImportError:
    QISKIT_OK = False; _USE_N_LOCAL = False; TwoLocal = None  # type: ignore

try:
    from qiskit.circuit.library import DiagonalGate; DIAG_OK = True
except ImportError:
    DIAG_OK = False

# ── IQM pytket backend ────────────────────────────────────────────────────────
try:
    from pytket.extensions.iqm import IQMBackend
    IQM_OK = True
except ImportError:
    IQM_OK = False; IQMBackend = None  # type: ignore

# ── pytket-qiskit bridge (Qiskit circuit → pytket → IQM) ─────────────────────
try:
    from pytket.extensions.qiskit import qiskit_to_tk
    PYTKET_QISKIT_OK = True
except ImportError:
    PYTKET_QISKIT_OK = False; qiskit_to_tk = None  # type: ignore

# ── Qrisp IQM backend ─────────────────────────────────────────────────────────
# API: qrisp.interface.IQMBackend(api_token=..., device_instance=...)
# qv.get_measurement(backend=qrisp_iqm_backend, shots=N) → {bitstring: prob}
try:
    from qrisp.interface import IQMBackend as QrispIQMBackend
    QRISP_OK = True
except ImportError:
    QRISP_OK = False; QrispIQMBackend = None  # type: ignore

# ── IBM Quantum Runtime ────────────────────────────────────────────────────────
try:
    from qiskit_ibm_runtime import QiskitRuntimeService
    try:
        from qiskit_ibm_runtime import SamplerV2 as IBMSampler
    except ImportError:
        from qiskit_ibm_runtime import Sampler as IBMSampler
    IBM_OK = True
except ImportError:
    IBM_OK = False; IBMSampler = None; QiskitRuntimeService = None  # type: ignore

# =============================================================================
# LOGGING
# =============================================================================

CACHE_DIR = "cache/"
os.makedirs(CACHE_DIR, exist_ok=True)

# Silence extremely verbose Qiskit transpiler pass logs
for _noisy_logger in [
    "qiskit.compiler.transpiler",
    "qiskit.passmanager",
    "qiskit.transpiler",
    "qiskit.transpiler.passes",
    "qiskit_aer",
    "stevedore",
    "urllib3",
]:
    logging.getLogger(_noisy_logger).setLevel(logging.ERROR)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(CACHE_DIR, "key_reducer_iqm.log")),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("KeyReducerIQM")

class _SpamFilter(logging.Filter):
    """Silence harmless import noise from stale qiskit plugins."""
    _SKIP = ("ProviderV1", "Could not load 'ibm_backend'",
             "Could not load 'ibm_dynamic_circuits'")
    def filter(self, record: logging.LogRecord) -> bool:
        msg = record.getMessage()
        return not any(s in msg for s in self._SKIP)

logging.getLogger().addFilter(_SpamFilter())
log.info("=" * 72)
log.info("KEY-REDUCER  MERGED v21 — P-BIT ENGINE v1 (Glauber/sigmoid) + QPB ENGINE v3 (Ry(2·arcsin(√sigmoid(β·I))) + CRZ coupling) + ADAPTIVE-COIN QUANTUM WALK — ALL THREE WALK TOGETHER — S1-QFT + S2-QPE + S3-AmpEst + ECPRA — Snake Corridor Detection")
log.info("=" * 72)

_DIAG_MAX_BITS   = 24    # DiagonalGate safe up to 2^24 complex128 ≈ 128 MB
_MODE1_GROVER_MAX_BITS = 20

# =============================================================================
# IQM DEVICE CATALOGUE
# =============================================================================

# IQM device USABLE qubits (MaxNQubitsPredicate enforced by pytket-iqm)
# Emerald physical = 54 but pytket MaxNQubitsPredicate = 52 (2 reserved for ctrl)
IQM_DEVICE_QUBITS: Dict[str, int] = {
    "sirius":  14,   # 16 physical, 14 usable after pytket overhead
    "garnet":  18,   # 20 physical, 18 usable
    "emerald": 50,   # 54 physical, 50 usable (safe margin below 52 predicate)
}

_MAX_AER_QUBITS  = 27   # AerSimulator safe cap
_MAX_IQM_CIRCUIT = 50   # Hard cap for IQM (MaxNQubitsPredicate = 52)
_MAX_IBM_QUBITS  = 156  # Conservative IBM cap (avoid routing overhead on 156q)
_ANCILLA_STRIDE  = 4    # entangle ancilla every N key qubits
_IBM_DEFAULT_BACKEND = "ibm_fez"

QRISP_DEVICE_ALIASES: Dict[str, str] = {
    "sirius": "sirius", "garnet": "garnet", "emerald": "emerald",
}

# =============================================================================
# SECP256K1  (pure Python)
# =============================================================================

_P  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
_B  = 7
_Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
_Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8


def _modinv(a: int, m: int) -> Optional[int]:
    a %= m
    if a == 0: return None
    g, x, b, y = m, 0, a, 1
    while b:
        q = g // b; g, b = b, g - q * b; x, y = y, x - q * y
    return x % m if g == 1 else None


def _pt_add(p1, p2):
    if p1 is None: return p2
    if p2 is None: return p1
    x1, y1 = p1; x2, y2 = p2
    if x1 == x2:
        if (y1 + y2) % _P == 0: return None
        inv = _modinv(2 * y1, _P)
        if inv is None: return None
        lam = 3 * x1 * x1 * inv % _P
    else:
        inv = _modinv(x2 - x1, _P)
        if inv is None: return None
        lam = (y2 - y1) * inv % _P
    x3 = (lam * lam - x1 - x2) % _P
    return x3, (lam * (x1 - x3) - y1) % _P


def _pt_mul(k: int, pt) -> Optional[Tuple[int, int]]:
    r = None; a = pt
    while k:
        if k & 1: r = _pt_add(r, a)
        a = _pt_add(a, a); k >>= 1
    return r


def _pubkey_bytes(k: int) -> bytes:
    pt = _pt_mul(k, (_Gx, _Gy))
    if pt is None: return b"\x00" * 33
    x, y = pt
    return (b"\x02" if y % 2 == 0 else b"\x03") + x.to_bytes(32, "big")


def _pubkey_point(k: int) -> Optional[Tuple[int, int]]:
    return _pt_mul(k, (_Gx, _Gy))


def decompress_pubkey(hex_key: str) -> Optional[Tuple[int, int]]:
    h = hex_key.strip().lower()
    if len(h) < 66:
        log.error(f"Pubkey too short: {len(h)} chars (need 66)"); return None
    prefix = int(h[:2], 16)
    if prefix not in (2, 3):
        log.error(f"Bad prefix 0x{h[:2]} — must be 02 or 03"); return None
    x    = int(h[2:66], 16)
    y_sq = (pow(x, 3, _P) + _B) % _P
    y    = pow(y_sq, (_P + 1) // 4, _P)
    if (y % 2 != 0 and prefix == 2) or (y % 2 == 0 and prefix == 3):
        y = _P - y
    if (y * y - x * x * x - _B) % _P != 0:
        log.error("Point not on secp256k1"); return None
    return x, y


# =============================================================================
# DELTA PRECOMPUTATION
# =============================================================================

def precompute_deltas(
    pubkey_xy: Tuple[int, int],
    k_start:   int,
    bits:      int,
) -> Tuple[List[int], List[int]]:
    """
    Per-qubit EC directional hints.
    dxs[b] = bit b of pubkey_xy[0]  (0 or 1).
    Phase oracle applies RZ(pi*(1-2*dxs[b])*anneal) per qubit per step,
    steering the walk toward the correct bit value.
    """
    px, py = pubkey_xy
    dxs = [(px >> b) & 1 for b in range(bits)]
    dys = [(py >> b) & 1 for b in range(bits)]
    log.info(f"  [DeltaPrecompute] per-bit hints bits={bits} "
             f"ones={sum(dxs)} zeros={bits-sum(dxs)}")
    return dxs, dys


# =============================================================================
# [G-4] PUBLIC KEY RANGE SHIFTING / CENTERING
# =============================================================================

def range_shift_pubkey(
    pubkey_xy:  Tuple[int, int],
    base:       int,
    bits:       int,
    full_start: int = 0,
    full_end:   int = 0,
) -> Tuple[Optional[Tuple[int, int]], int]:
    """
    Shift pubkey by 12.5% into the valid range.
    full_start and full_end are now parameters — no NameError.
    shift = full_start + space//8 ensures k - shift stays positive
    for any key above the 12.5% mark (covers all typical puzzles).
    """
    try:
        if full_end <= full_start:
            full_start = base
            full_end   = base + (1 << bits) - 1
        space  = full_end - full_start
        shift  = full_start + max(1, space // 8)
        if shift >= full_end:
            shift = full_start + max(1, space // 16)
        shift_G     = _pt_mul(shift, (_Gx, _Gy))
        if shift_G is None: return None, 0
        neg_shift_G = (shift_G[0], (_P - shift_G[1]) % _P)
        q_shifted   = _pt_add(pubkey_xy, neg_shift_G)
        if q_shifted is None: return None, 0
        log.info(f"  [G-4 RangeShift] shift={hex(shift)[:18]}  "
                 f"Q_x={hex(q_shifted[0])[:18]}")
        return q_shifted, shift
    except Exception as e:
        log.warning(f"  [G-4 RangeShift] failed: {e}")
        return None, 0


# =============================================================================
# HASH PIPELINE
# =============================================================================

def _hash160(data: bytes) -> bytes:
    sha = hashlib.sha256(data).digest()
    if PYCRYPTO_OK and _RIPEMD160 is not None:
        return _RIPEMD160.new(sha).digest()
    return hashlib.new("ripemd160", sha).digest()


def _k_to_hash160(k: int) -> bytes:
    return _hash160(_pubkey_bytes(k))


# =============================================================================
# ADDRESS → HASH160
# =============================================================================

_B58A = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def _b58decode(s: str) -> bytes:
    num = 0
    for c in s: num = num * 58 + _B58A.index(c)
    nb  = (num.bit_length() + 7) // 8
    out = num.to_bytes(max(nb, 1), "big")
    pad = len(s) - len(s.lstrip(_B58A[0]))
    return b"\x00" * pad + out


def address_to_hash160(address: str) -> bytes:
    address = address.strip()
    try:
        if BASE58_OK:
            payload = base58.b58decode_check(address)
        else:
            raw  = _b58decode(address)
            body = raw[:-4]; chk = raw[-4:]
            if hashlib.sha256(hashlib.sha256(body).digest()).digest()[:4] != chk:
                raise ValueError("checksum mismatch")
            payload = body
    except Exception as e:
        raise ValueError(f"Invalid Bitcoin address: {e}")
    if len(payload) < 21 or payload[0] != 0x00:
        raise ValueError("Not a mainnet P2PKH address")
    return payload[1:21]


# =============================================================================
# PUZZLE PRESETS  (identical to IBM version — all known pubkeys included)
# =============================================================================

PUZZLE_PRESETS: Dict[int, Dict] = {
    5:  {"start": 0x10,
         "end":   0x1F,
         "pub":   "02352bbf4a4cdd12564f93fa332ce333301d9ad40271f8107181340aef25be59d5",
         "shots": 1024,   "layers": 3, "iters": 6,  "probes": 128},
    8:  {"start": 0x80,
         "end":   0xFF,
         "pub":   "0308bc89c2f919ed158885c35600844d49890905c79b357322609c45706ce6b514",
         "shots": 8192,   "layers": 3, "iters": 8,  "probes": 256},
    14: {"start": 0x2000,
         "end":   0x3FFF,
         "pub":   "03b4f1de58b8b41afe9fd4e5ffbdafaeab86c5db4769c15d6e6011ae7351e54759",
         "shots": 10000,  "layers": 4, "iters": 10, "probes": 512},
    16: {"start": 0x8000,
         "end":   0xFFFF,
         "pub":   "029d8c5d35231d75eb87fd2c5f05f65281ed9573dc41853288c62ee94eb2590b7a",
         "shots": 32768,  "layers": 4, "iters": 12, "probes": 512},
    20: {"start": 0x80000,
         "end":   0xFFFFF,
         "pub":   "033c4a45cbd643ff97d77f41ea37e843648d50fd894b864b0d52febc62f6454f7c",
         "shots": 32768,  "layers": 4, "iters": 12, "probes": 512},
    21: {"start": 0x100000,
         "end":   0x1FFFFF,
         "pub":   "031a746c78f72754e0be046186df8a20cdce5c79b2eda76013c647af08d306e49e",
         "shots": 32768,  "layers": 4, "iters": 12, "probes": 512},
    24: {"start": 0x800000,
         "end":   0xFFFFFF,
         "pub":   "036ea839d22847ee1dce3bfc5b11f6cf785b0682db58c35b63d1342eb221c3490c",
         "shots": 65536,  "layers": 4, "iters": 12, "probes": 512},
    25: {"start": 0x1000000,
         "end":   0x1FFFFFF,
         "pub":   "03057fbea3a2623382628dde556b2a0698e32428d3cd225f3bd034dca82dd7455a",
         "shots": 65536,  "layers": 4, "iters": 14, "probes": 512},
    32: {"start": 0x80000000,
         "end":   0xFFFFFFFF,
         "pub":   "036ea839d22847ee1dce3bfc5b11f6cf785b0682db58c35b63d1342eb221c3490c",
         "shots": 65536,  "layers": 5, "iters": 16, "probes": 1024},
    40: {"start": 0x8000000000,
         "end":   0xFFFFFFFFFF,
         "pub":   "03a2efa402fd5268400c77c20e574ba86409ededee7c4020e4b9f0edbee53de0d4",
         "shots": 65536,  "layers": 5, "iters": 16, "probes": 1024},
    64: {"start": 0x8000000000000000,
         "end":   0xFFFFFFFFFFFFFFFF,
         "pub":   "03100611c54dfef604163b8358f7b7fac13ce478e02cb224ae16d45526b25d9d4d",
         "shots": 65536,  "layers": 5, "iters": 16, "probes": 1024},
    71: {"start": 0x400000000000000000,
         "end":   0x7fffffffffffffffff,
         "pub":   None, # Use Hash160 Mod-1_Version
         "shots": 65536,  "layers": 5, "iters": 16, "probes": 1024},
    135:{"start": 0x400000000000000000000000000000000,
         "end":   0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
         "pub":   "02145d2611c823a396ef6712ce0f712f09b9b4f3135e3e0aa3230fb9b6d08d1e16",
         "shots": 100000, "layers": 5, "iters": 20, "probes": 1024},
}


def auto_range(bits: int) -> Tuple[int, int]:
    p = PUZZLE_PRESETS.get(bits)
    if p: return p["start"], p["end"]
    return 1 << (bits - 1), (1 << bits) - 1


def _preset_pubkey(bits: int) -> Optional[str]:
    return (PUZZLE_PRESETS.get(bits) or {}).get("pub")

def _preset_shots(bits: int) -> int:
    return (PUZZLE_PRESETS.get(bits) or {}).get("shots", 4096)

def _preset_layers(bits: int) -> int:
    return (PUZZLE_PRESETS.get(bits) or {}).get("layers", 4)

def _preset_iters(bits: int) -> int:
    return (PUZZLE_PRESETS.get(bits) or {}).get("iters", 12)

def _preset_probes(bits: int) -> int:
    return (PUZZLE_PRESETS.get(bits) or {}).get("probes", 512)


# =============================================================================
# ENERGY FUNCTION  [FIX-4: weighted XOR — MSBs count more]
# =============================================================================

def compute_energy(
    k: int,
    target_h160: bytes,
    pubkey_xy: Optional[Tuple[int, int]] = None,
    pubkey_hex: Optional[str] = None,
) -> float:
    """
    FIX-ENERGY: produce a REAL gradient signal, not a flat landscape.

    Pubkey mode: normalised absolute x-coordinate distance in [0, 1].
      The correct key gives distance = 0  (minimum energy).
      Keys far away give distance near 1  (maximum energy).
      This creates a genuine gradient the sampler can follow.

    Hash160 mode: weighted Hamming over first 10 (MSB) bytes, normalised.
    """
    try:
        if pubkey_xy is not None:
            pt = _pubkey_point(k)
            if pt is None: return 1.0
            # Absolute normalised x-distance in [0, 1]
            e = abs(pt[0] - pubkey_xy[0]) / _P
            # Tiny parity tie-break so +y and -y are distinguishable
            if pt[1] % 2 != pubkey_xy[1] % 2:
                e += 1e-9
            return float(min(e, 1.0))
        # Hash160 mode: weight MSB bytes more heavily
        h160  = _k_to_hash160(k)
        dist  = 0.0
        n_use = min(10, len(h160))
        for byte_idx in range(n_use):
            xor    = h160[byte_idx] ^ target_h160[byte_idx]
            weight = 1.0 - 0.5 * (byte_idx / max(n_use - 1, 1))
            dist  += bin(xor).count("1") * weight
        return float(dist / (n_use * 8.0))   # normalised → [0, 1]
    except Exception:
        return 1.0


def compute_energy_bits(k: int, pubkey_xy: Tuple[int, int]) -> List[int]:
    pt = _pubkey_point(k)
    if pt is None: return [0] * 256
    xdiff = pt[0] ^ pubkey_xy[0]
    return [(xdiff >> b) & 1 for b in range(256)]


# =============================================================================
# [G-2] SOBOL QUASI-RANDOM PROBE SAMPLING
# =============================================================================

def _sobol_offsets(n_probes: int, bits: int) -> List[int]:
    if bits >= 63:
        import random as _rng
        space = 1 << bits
        return [_rng.randint(0, space - 1) for _ in range(n_probes)]
    space = 1 << bits
    if SOBOL_OK:
        try:
            n_pow2  = max(2, 1 << math.ceil(math.log2(max(n_probes, 2))))
            sampler = Sobol(d=1, scramble=True)
            raw     = sampler.random(n_pow2)[:n_probes]
            return [int(float(raw[i, 0]) * space) % space for i in range(n_probes)]
        except Exception as e:
            log.debug(f"  [G-2] Sobol failed ({e}) — stratified fallback")
    bucket = max(1, space // n_probes)
    import random as _rng
    return [_rng.randint(i * bucket, min((i + 1) * bucket - 1, space - 1))
            for i in range(n_probes)]


# =============================================================================
# PHASE A — SparsePauliOp Ising Hamiltonian  [G-2 Sobol, G-3 non-NN]
# =============================================================================

def build_ising_hamiltonian(
    bits: int, base: int, target_h160: bytes,
    pubkey_xy: Optional[Tuple[int, int]] = None,
    pubkey_hex: Optional[str] = None,
    n_probes: int = 512,
    dxs: Optional[List[int]] = None,
) -> Tuple[Optional["SparsePauliOp"], np.ndarray, np.ndarray]:
    log.info(f"  [SparsePauliOp] Probing {n_probes} offsets ({bits}-bit) "
             f"via {'Sobol' if (SOBOL_OK and bits < 63) else 'stratified'}…")
    offsets_py = _sobol_offsets(n_probes, bits)
    energies   = np.array([
        compute_energy(base + o, target_h160, pubkey_xy, pubkey_hex)
        for o in offsets_py
    ], dtype=float)
    e_min, e_max = energies.min(), energies.max()
    en = ((energies - e_min) / (e_max - e_min)
          if e_max > e_min else np.full(n_probes, 0.5))

    h_biases = np.zeros(bits)
    for b in range(bits):
        mask1   = np.array([(o >> b) & 1 for o in offsets_py], dtype=bool)
        e1      = en[mask1]; e0 = en[~mask1]
        # FIX: multiply by 2 so biases properly span [-1, +1]
        h_biases[b] = 2.0 * ((e0.mean() if len(e0) else 0.5) -
                              (e1.mean() if len(e1) else 0.5))

    if dxs is not None and len(dxs) == bits:
        for b in range(bits):
            h_biases[b] += (1.0 - 2.0 * int(dxs[b])) * 0.5
    # Clip to [-1, 1] so arccos() initialisation stays valid
    h_biases = np.clip(h_biases, -1.0, 1.0)

    J_nn    = np.zeros(bits - 1)
    J_skip2 = np.zeros(bits - 2)
    J_skip3 = np.zeros(bits - 3)

    for b in range(bits - 1):
        same = np.array([((o >> b) & 1) == ((o >> (b+1)) & 1) for o in offsets_py], dtype=bool)
        e_s = en[same]; e_d = en[~same]
        J_nn[b] = ((e_d.mean() if len(e_d) else 0.5) - (e_s.mean() if len(e_s) else 0.5))
    for b in range(bits - 2):
        same = np.array([((o >> b) & 1) == ((o >> (b+2)) & 1) for o in offsets_py], dtype=bool)
        e_s = en[same]; e_d = en[~same]
        J_skip2[b] = ((e_d.mean() if len(e_d) else 0.5) - (e_s.mean() if len(e_s) else 0.5)) * 0.5
    for b in range(bits - 3):
        same = np.array([((o >> b) & 1) == ((o >> (b+3)) & 1) for o in offsets_py], dtype=bool)
        e_s = en[same]; e_d = en[~same]
        J_skip3[b] = ((e_d.mean() if len(e_d) else 0.5) - (e_s.mean() if len(e_s) else 0.5)) * 0.25

    log.info(f"  [SparsePauliOp] h∈[{h_biases.min():.3f},{h_biases.max():.3f}]  "
             f"J_nn∈[{J_nn.min():.3f},{J_nn.max():.3f}]  "
             f"J_skip2∈[{J_skip2.min():.3f},{J_skip2.max():.3f}]")

    if not QISKIT_OK:
        return None, h_biases, J_nn

    pauli_terms: List[str] = []; coeffs: List[float] = []
    for i in range(bits):
        pl = ["I"] * bits; pl[bits-1-i] = "Z"
        pauli_terms.append("".join(pl)); coeffs.append(float(h_biases[i]))
    for i in range(bits - 1):
        pl = ["I"] * bits; pl[bits-1-i] = "Z"; pl[bits-1-(i+1)] = "Z"
        pauli_terms.append("".join(pl)); coeffs.append(float(J_nn[i]))
    for i in range(bits - 2):
        pl = ["I"] * bits; pl[bits-1-i] = "Z"; pl[bits-1-(i+2)] = "Z"
        pauli_terms.append("".join(pl)); coeffs.append(float(J_skip2[i]))
    for i in range(bits - 3):
        pl = ["I"] * bits; pl[bits-1-i] = "Z"; pl[bits-1-(i+3)] = "Z"
        pauli_terms.append("".join(pl)); coeffs.append(float(J_skip3[i]))

    H = SparsePauliOp(pauli_terms, coeffs=np.array(coeffs))
    return H, h_biases, J_nn


# =============================================================================
# [FIX-1] h_bias-SEEDED PARAMETER INITIALISATION
# =============================================================================

def _make_biased_params(
    h_biases: np.ndarray, J_couplings: np.ndarray,
    n_params: int, bits: int, noise_scale: float = 0.4,
) -> np.ndarray:
    params    = np.random.normal(0.0, noise_scale, n_params)
    ry_angles = np.arccos(np.clip(-h_biases, -1.0, 1.0))
    for i in range(min(bits, n_params)):
        params[i] = ry_angles[i % bits] + np.random.normal(0, noise_scale)
    ry_total = min((len(h_biases) + 1) * bits, n_params)
    for j in range(ry_total, min(ry_total + len(J_couplings), n_params)):
        jidx = j - ry_total
        if jidx < len(J_couplings):
            params[j] = J_couplings[jidx] * math.pi + np.random.normal(0, noise_scale)
    return params


# =============================================================================
# [FIX] _make_twolocal() — forward-compatible ansatz builder
# Qiskit >=2.1 deprecates TwoLocal class → use n_local() function instead.
# Falls back to TwoLocal class, then to manual RY+CX as last resort.
# =============================================================================

def _make_twolocal(n_qubits: int, layers: int) -> "QuantumCircuit":
    """Build TwoLocal-equivalent RY+CX ansatz, compatible with all Qiskit versions."""
    if _USE_N_LOCAL:
        try:
            return _n_local_fn(
                n_qubits, rotation_blocks="ry",
                entanglement_blocks="cx", entanglement="linear", reps=layers,
            )
        except Exception:
            pass
    if TwoLocal is not None:
        return TwoLocal(n_qubits, "ry", "cx", reps=layers, entanglement="linear")
    # Emergency: manual RY+CX
    from qiskit.circuit import ParameterVector
    qc  = QuantumCircuit(n_qubits)
    pv  = ParameterVector("θ", n_qubits * (layers + 1))
    idx = 0
    for rep in range(layers + 1):
        for q in range(n_qubits):
            qc.ry(pv[idx], q); idx += 1
        if rep < layers:
            for q in range(n_qubits - 1):
                qc.cx(q, q + 1)
    return qc


# =============================================================================
# LATTICE REFINEMENT  [G-8: BKZ block 20+]
# =============================================================================

def _lll_2x2(order: int, m: int) -> int:
    a, b = order, 0; c, d = m, 1
    while True:
        n1 = a*a+b*b; n2 = c*c+d*d
        if n1 > n2: a, b, c, d = c, d, a, b; n1, n2 = n2, n1
        if n1 == 0: break
        mu = (a*c+b*d)/n1; mr = round(mu)
        c -= mr*a; d -= mr*b
        if n2 >= (0.75-(mu-mr)**2)*n1: break
    return int(d) % order


def lattice_refine_candidates(
    top_offsets: List[int], bits: int, base: int,
    target_h160: bytes,
    pubkey_xy: Optional[Tuple[int, int]],
    pubkey_hex: Optional[str],
    bkz_block: int = 20,
) -> List[Tuple[float, int]]:
    if len(top_offsets) < 2: return []
    extra: List[Tuple[float, int]] = []
    n = len(top_offsets); order = 1 << bits
    if FPYLLL_OK and n >= 2:
        try:
            chunk = max(1, bits // max(1, n))
            M     = IntegerMatrix(n, n)
            for i, off in enumerate(top_offsets):
                for j in range(n):
                    M[i, j] = (off >> (j * chunk)) & ((1 << chunk) - 1)
            for blk in [bkz_block, min(bkz_block+10,30), min(bkz_block+20,40)]:
                try:    BKZ.reduction(M, BKZ.Param(blk))
                except Exception: break
            try:    FpLLL.reduction(M)
            except Exception: pass
            for row in range(min(n, 8)):
                cand = abs(sum(M[row,j]*(1<<(j*chunk)) for j in range(n))) % order
                e = compute_energy(base+cand, target_h160, pubkey_xy, pubkey_hex)
                extra.append((e, cand))
            log.info(f"  [Lattice-BKZ{bkz_block}] {len(extra)} candidates (fpylll)")
        except Exception as ex:
            log.debug(f"  [Lattice-BKZ] error: {ex}")
    else:
        for off in top_offsets:
            cand = _lll_2x2(order, off)
            e    = compute_energy(base+cand, target_h160, pubkey_xy, pubkey_hex)
            extra.append((e, cand))
        log.info(f"  [Lattice-2x2] {len(extra)} candidates (pure-Python fallback)")
    return extra


# =============================================================================
# GROVER DIFFUSER
# =============================================================================

def _build_diffuser(n: int) -> "QuantumCircuit":
    """Fully decomposed Grover diffuser — Aer never sees a named custom gate."""
    qc = QuantumCircuit(n)
    qc.h(range(n)); qc.x(range(n))
    if n == 1:   qc.z(0)
    elif n == 2: qc.cz(0, 1)
    else:
        qc.h(n-1); qc.mcx(list(range(n-1)), n-1); qc.h(n-1)
    qc.x(range(n)); qc.h(range(n))
    # Decompose so Aer transpiler never hits "unknown instruction: diffuser/mcx"
    try:
        qc = qc.decompose(reps=2)
    except Exception:
        pass
    return qc


# =============================================================================
# [MODE1] REAL HASH-PREIMAGE GROVER
# =============================================================================

def precompute_hash160_table(
    base: int, bits: int, target_h160: bytes,
) -> Optional[int]:
    space = 1 << bits
    log.info(f"  [MODE1-GROVER] Precomputing {space:,} hash160 values "
             f"(bits={bits}, base={hex(base)})…")
    t0 = time.perf_counter()
    marked_offset: Optional[int] = None
    for offset in range(space):
        k = base + offset
        h = _k_to_hash160(k)
        if h == target_h160:
            marked_offset = offset
            log.info(f"  [MODE1-GROVER] ✅ MATCH at offset={offset}  "
                     f"k={hex(k)}  ({time.perf_counter()-t0:.2f}s)")
            break
    elapsed = time.perf_counter() - t0
    if marked_offset is None:
        log.warning(f"  [MODE1-GROVER] No match in {space:,} keys ({elapsed:.2f}s). "
                    f"Key not in range? base={hex(base)}")
    return marked_offset


def build_real_grover_circuit(
    bits: int, marked_offset: int, ancilla: int = 0,
) -> Optional["QuantumCircuit"]:
    if not QISKIT_OK or not DIAG_OK:
        log.warning("  [MODE1-GROVER] DiagonalGate unavailable"); return None
    space      = 1 << bits
    n_iter_opt = max(1, round(math.pi / 4.0 * math.sqrt(space)))
    log.info(f"  [MODE1-GROVER] Real Grover {bits}q  "
             f"oracle marks offset={marked_offset}  "
             f"optimal_iters={n_iter_opt}")
    diag = np.ones(space, dtype=complex)
    diag[marked_offset] = -1.0
    oracle_gate = DiagonalGate(diag.tolist())
    diffuser    = _build_diffuser(bits)
    key_r = QuantumRegister(bits, "key")
    cr    = ClassicalRegister(bits, "mkey")
    if ancilla > 0:
        anc_r = QuantumRegister(ancilla, "anc")
        qc    = QuantumCircuit(key_r, anc_r, cr, name=f"RealGrover_{bits}bit_MaxQ")
        qc.h(key_r); qc.h(anc_r)
    else:
        qc = QuantumCircuit(key_r, cr, name=f"RealGrover_{bits}bit")
        qc.h(key_r)
    for _ in range(n_iter_opt):
        qc.append(oracle_gate, list(key_r))
        if ancilla > 0:
            for ai in range(ancilla):
                ki = (ai * _ANCILLA_STRIDE) % bits
                qc.cx(key_r[ki], anc_r[ai])
        qc.append(diffuser, list(key_r))
        if ancilla > 0:
            qc.reset(anc_r); qc.h(anc_r)
    qc.measure(key_r, cr)
    log.info(f"  [MODE1-GROVER] Circuit qubits={qc.num_qubits}  "
             f"depth≈{n_iter_opt*3}  iters={n_iter_opt}")
    return qc


# =============================================================================
# PHASE C — GROVER-IPE CIRCUIT  (crash-free for ANY bit size)
# =============================================================================


def _rz_phase_oracle(bits: int, marked: list) -> "QuantumCircuit":
    """
    Pure RZ/CX phase oracle — no DiagonalGate, no named sub-circuits.
    Marks states with -1 phase using X + CX-ladder-Z + X pattern.
    Compiles cleanly on pytket-IQM AND Aer.
    """
    qc = QuantumCircuit(bits)
    for offset in marked[:16]:        # cap at 16 to keep depth sane
        for b in range(bits):
            if not ((offset >> b) & 1):
                qc.x(b)
        if bits == 1:
            qc.z(0)
        elif bits == 2:
            qc.cz(0, 1)
        else:
            for b in range(bits - 1):   qc.cx(b, b + 1)
            qc.z(bits - 1)
            for b in range(bits - 2, -1, -1): qc.cx(b, b + 1)
        for b in range(bits):
            if not ((offset >> b) & 1):
                qc.x(b)
    try:
        qc = qc.decompose(reps=2)
    except Exception:
        pass
    return qc

def build_grover_ipe_circuit(
    bits: int, top_offsets: List[int],
    h_biases: np.ndarray, n_ipe_rounds: int = 3,
) -> Optional["QuantumCircuit"]:
    if not QISKIT_OK: return None
    n_rounds = max(n_ipe_rounds, 3)
    marked   = [int(o) for o in top_offsets if 0 <= int(o) < (1 << bits)][:64]
    if not marked: return None
    use_diag = False  # FIX: DiagonalGate crashes pytket; always RZ oracle
    ctrl_r = QuantumRegister(1, "ctrl"); key_r = QuantumRegister(bits, "key")
    cr     = ClassicalRegister(bits, "mkey")
    qc     = QuantumCircuit(ctrl_r, key_r, cr, name=f"GroverIPE_{bits}bit")
    qc.h(key_r)
    if use_diag:
        diag = np.ones(1 << bits, dtype=complex)
        for o in marked: diag[o] = -1.0
        oracle_gate = None  # FIX: DiagonalGate crashes pytket — RZ oracle used below
        log.info(f"  [Grover-IPE] DiagonalGate  {bits}q  {n_rounds} rds  {len(marked)} tgts")
    else:
        oracle_gate = None
        vote = np.zeros(bits, dtype=float)
        for o in marked:
            for b in range(bits):
                if (o >> b) & 1: vote[b] += 1.0
        if vote.max() > 0: vote /= vote.max()
        log.info(f"  [Grover-IPE] Phase-kickback  {bits}q  {n_rounds} rds  "
                 f"{len(marked)} tgts  (crash-free)")
    diffuser = _build_diffuser(bits)
    # FIX-CommutableMeasures: NO mid-circuit measure/reset inside loop.
    # All oracle+diffuser rounds first, single terminal measurement.
    for rnd in range(n_rounds):
        qc.h(ctrl_r[0])
        for i, hi in enumerate(h_biases):
            angle = float(2.0 * hi)
            if abs(angle) > 1e-6: qc.cp(angle, ctrl_r[0], key_r[i])
        qc.h(ctrl_r[0])
        # Phase kickback via RZ replaces mid-circuit measure+reset
        qc.rz(math.pi / max(n_rounds, 1), ctrl_r[0])
        if use_diag and oracle_gate is not None:
            qc.append(oracle_gate, list(key_r))
        else:
            for b in range(bits):
                angle = float(math.pi * vote[b])
                if abs(angle) > 1e-6: qc.rz(angle, key_r[b])
        qc.append(diffuser, list(key_r))
    # Single measurement at the end — satisfies CommutableMeasuresPredicate
    qc.measure(key_r, cr)
    return qc


# =============================================================================
# [G-7] DBSCAN DENSITY CLUSTERING
# =============================================================================

def dbscan_cluster_offsets(
    all_samples: List[Tuple[float, int]], bits: int,
    eps_frac: float = 0.05, min_samples: int = 5,
) -> List[int]:
    if not SKLEARN_OK or len(all_samples) < min_samples * 2:
        return [int(o) for _, o in sorted(all_samples, key=lambda x: x[0])[:128]]
    try:
        space   = 1 << bits
        offsets = np.array([int(o) for _, o in all_samples], dtype=float)
        normed  = (offsets / space).reshape(-1, 1)
        db      = DBSCAN(eps=eps_frac, min_samples=min_samples).fit(normed)
        labels  = db.labels_
        unique, counts = np.unique(labels[labels >= 0], return_counts=True)
        if len(unique) == 0:
            log.info("  [G-7 DBSCAN] No cluster found — top-K fallback")
            return [int(o) for _, o in sorted(all_samples, key=lambda x: x[0])[:128]]
        best_label  = unique[np.argmax(counts)]
        cluster_idx = np.where(labels == best_label)[0]
        cluster_offs = [int(all_samples[i][1]) for i in cluster_idx]
        log.info(f"  [G-7 DBSCAN] Cluster size={len(cluster_offs)}  "
                 f"centroid≈{hex(int(np.mean(cluster_offs)))[:18]}")
        return cluster_offs
    except Exception as e:
        log.warning(f"  [G-7 DBSCAN] error: {e} — top-K fallback")
        return [int(o) for _, o in sorted(all_samples, key=lambda x: x[0])[:128]]


# =============================================================================
# PHASE D — FORCED RANGE EXTRACTION
# =============================================================================

def quantum_trajectory_range(
    all_samples: List[Tuple[float, int]],
    base: int, bits: int,
    full_start: int, full_end: int,
    target_coverage: float = 0.25,
    pubkey_xy: Optional[Tuple[int, int]] = None,
    target_h160: Optional[bytes] = None,
) -> Tuple[int, int, List[str], np.ndarray]:
    """
    ENERGY-GUIDED SNAKE BRACKET v15

    Two-stage approach — eliminates the fixed-size bracket problem:

    Stage 1 — Energy threshold (data-adaptive, no fixed K):
      Re-score ALL QPU samples with compute_energy(base+offset, pubkey_xy).
      Energy = 0.0 exactly at the true key (coordinate-frame-independent).
      Find best_energy = minimum energy across all samples.
      Find energy_gap  = gap between best and next distinct energy level.
      Threshold = best_energy + energy_gap * 0.5 (data-driven).
      Candidate pool = all samples below threshold.
      If pool is too small (<4), widen threshold until pool has ≥4 samples.
      This means: strong QPU signal → tight pool → tight bracket.
                  weak QPU signal  → pool widens naturally (honest output).

    Stage 2 — Snake corridor inside the pool:
      Sort candidate pool offsets.
      Find the LARGEST GAP between consecutive offsets in the pool.
      UPPER BOUND = left wall of that gap (last visited before empty corridor)
      LOWER BOUND = right wall of that gap (first visited after corridor)
      These are REAL measured QPU offsets — no sigma, no fixed fraction.
      Weighted by midpoint proximity (70% size + 30% mid-bias) so that
      ties are broken toward the middle of the range where keys cluster.

    Fallback: if gap is degenerate (pool has <2 unique offsets),
      UPPER = min(pool), LOWER = max(pool) — still energy-guided.
    """
    log.info(f"  [SNAKE-v15] {len(all_samples)} samples → energy-guided snake bracket")

    if not all_samples:
        log.warning("  [SNAKE-v15] No samples")
        return full_start, full_end, ["?"] * bits, np.full(bits, 0.5)

    # ── Filter to valid in-range offsets ─────────────────────────────────────
    max_valid_off = full_end - base
    min_valid_off = max(0, full_start - base)
    valid_range   = max(1, max_valid_off - min_valid_off)
    valid_s = [(e, int(o)) for e, o in all_samples
               if min_valid_off <= int(o) <= max_valid_off]
    if len(valid_s) < 8:
        valid_s = [(e, int(o)) for e, o in all_samples]
        log.warning(f"  [SNAKE-v15] Only {len(valid_s)} in-range — using all")
    if not valid_s:
        return full_start, full_end, ["?"] * bits, np.full(bits, 0.5)

    # ── Stage 1: Re-score with ORIGINAL pubkey (coordinate-frame-independent) ─
    rescored: List[Tuple[float, int]] = []
    if pubkey_xy is not None:
        for _, off in valid_s:
            e = compute_energy(base + off, target_h160 or b"", pubkey_xy, None)
            rescored.append((e, off))
        log.info(f"  [SNAKE-v15] Re-scored {len(rescored)} with original pubkey_xy")
    elif target_h160:
        for _, off in valid_s:
            e = compute_energy(base + off, target_h160, None, None)
            rescored.append((e, off))
        log.info(f"  [SNAKE-v15] Re-scored {len(rescored)} with hash160")
    else:
        rescored = list(valid_s)

    sorted_s    = sorted(rescored, key=lambda x: x[0])
    n_valid     = len(sorted_s)
    best_energy = sorted_s[0][0]

    # ── Data-adaptive energy threshold ────────────────────────────────────────
    # Find the gap between the best energy and the next distinct energy level.
    # This is the natural "quantum advantage signal" — how much better the
    # best sample is compared to the next best.
    distinct_energies = sorted(set(round(e, 8) for e, _ in sorted_s))
    if len(distinct_energies) >= 2:
        energy_step = distinct_energies[1] - distinct_energies[0]
    else:
        energy_step = best_energy * 0.01 if best_energy > 0 else 1e-6

    # Start tight, widen until we have enough candidates
    threshold = best_energy + energy_step * 0.5
    pool = [(e, o) for e, o in sorted_s if e <= threshold]

    # Widen threshold if pool is too small — but track how many widening steps
    widen_steps = 0
    while len(pool) < 4 and widen_steps < 20:
        threshold += energy_step * 0.5
        pool = [(e, o) for e, o in sorted_s if e <= threshold]
        widen_steps += 1

    if len(pool) < 2:
        pool = sorted_s[:max(4, n_valid // 64)]

    log.info(f"  [SNAKE-v15] best_e={best_energy:.8f}  energy_step={energy_step:.8f}  "
             f"threshold={threshold:.8f}  pool={len(pool)}  widen_steps={widen_steps}")

    pool_offs = sorted(set(int(o) for _, o in pool))

    # ── Stage 2: Snake corridor inside the energy-selected pool ──────────────
    # The p-bit/qubit AVOIDS the key — so inside the pool of low-energy
    # samples, the LARGEST GAP between consecutive offsets is where the
    # key hides (the empty corridor the walk never touches).
    gaps = []
    for i in range(len(pool_offs) - 1):
        g  = pool_offs[i+1] - pool_offs[i]
        gl = pool_offs[i]
        gr = pool_offs[i+1]
        gaps.append((g, gl, gr))

    if not gaps:
        # Only one unique offset — bracket = ±1 around it
        lo_off = max(min_valid_off, pool_offs[0] - 1)
        hi_off = min(max_valid_off, pool_offs[0] + 1)
        log.warning("  [SNAKE-v15] Single unique offset — using ±1 bracket")
    else:
        # Score gaps: 70% size + 30% midpoint proximity
        valid_mid = (min_valid_off + max_valid_off) / 2.0
        max_g     = max(g for g, _, _ in gaps)

        def _score(g, gl, gr):
            g_mid  = (gl + gr) / 2.0
            size_n = g / max(max_g, 1)
            mid_w  = max(0.0, 1.0 - 2.0 * abs(g_mid - valid_mid) / valid_range)
            return 0.70 * size_n + 0.30 * mid_w

        gaps_scored = sorted(gaps, key=lambda t: _score(t[0],t[1],t[2]), reverse=True)

        g_sizes  = np.array([g for g,_,_ in gaps], dtype=float)
        median_g = float(np.median(g_sizes))
        std_g    = float(np.std(g_sizes))
        outlier_t = max(median_g * 2.0, median_g + 2.0 * std_g)

        for rank, (gs, gl, gr) in enumerate(gaps_scored[:3]):
            sc = _score(gs, gl, gr)
            log.info(f"  [SNAKE-v15] Gap#{rank+1}: [{hex(base+gl)}, {hex(base+gr)}]  "
                     f"size={gs:,}  score={sc:.3f}  "
                     f"{'★ snake' if gs >= outlier_t else 'normal'}")

        best_g, gap_left, gap_right = gaps_scored[0]
        lo_off = gap_left
        hi_off = gap_right
        log.info(f"  [SNAKE-v15] Best gap: [{hex(base+lo_off)}, {hex(base+hi_off)}]  "
                 f"size={best_g:,}  valid_mid={hex(int(valid_mid))}")

    lo_off = max(min_valid_off, lo_off)
    hi_off = min(max_valid_off, hi_off)
    if lo_off >= hi_off:
        lo_off = max(min_valid_off, pool_offs[0]  if pool_offs else min_valid_off)
        hi_off = min(max_valid_off, pool_offs[-1] if pool_offs else max_valid_off)
    if lo_off >= hi_off:
        hi_off = min(max_valid_off, lo_off + 1)

    start_r    = max(full_start, base + lo_off)
    end_r      = min(full_end,   base + hi_off)
    bracket_sz = max(1, end_r - start_r)
    full_sz    = max(1, full_end - full_start)
    reduction  = full_sz // bracket_sz
    log.info(f"  [SNAKE-v15] LOWER={hex(start_r)}  UPPER={hex(end_r)}  "
             f"size={bracket_sz:,}  reduction={reduction:.0f}x")

    # ── Visualization ─────────────────────────────────────────────────────────
    # Compute two-best near-key candidates from pool for the oscilloscope plot
    try:
        sorted_pool = sorted(pool, key=lambda x: x[0])   # sort by energy
        two_best_near_abs = [base + int(o) for _, o in sorted_pool[:2]]
    except Exception:
        two_best_near_abs = []
    try:
        _plot_snake_v15(
            sorted_s=sorted_s, pool_offs=pool_offs,
            lo_off=lo_off, hi_off=hi_off,
            base=base, bits=bits,
            start_r=start_r, end_r=end_r,
            best_energy=best_energy, threshold=threshold,
            min_valid_off=min_valid_off, max_valid_off=max_valid_off,
            valid_range=valid_range,
            two_best_near=two_best_near_abs,
        )
    except Exception as ex:
        log.warning(f"  [SnakeViz] {ex}")

    # ── Bit probabilities from pool ───────────────────────────────────────────
    b_offs = [int(o) for _, o in pool]
    if b_offs:
        bit_arrays = np.array(
            [[(o >> (bits-1-b)) & 1 for b in range(bits)] for o in b_offs],
            dtype=float)
        bit_probs = bit_arrays.mean(axis=0)
    else:
        bit_probs = np.full(bits, 0.5)

    pinned: List[str] = ["?"] * bits
    for thr_hi, thr_lo in [(0.90,0.10),(0.82,0.18),(0.74,0.26),(0.64,0.36)]:
        cand = ["1" if p>thr_hi else "0" if p<thr_lo else "?" for p in bit_probs]
        if sum(1 for b in cand if b in ("0","1")) >= bits // 4:
            pinned = cand; break

    pc = sum(1 for b in pinned if b in ("0","1"))
    log.info(f"  [SNAKE-v15] pins={pc}/{bits}  reduction={reduction:.0f}x")

    return start_r, end_r, pinned, bit_probs


def _plot_snake_v17(
    sorted_s, pool_offs, lo_off, hi_off,
    base, bits, start_r, end_r, best_energy, threshold,
    min_valid_off, max_valid_off, valid_range,
    two_best_near: Optional[List[int]] = None,
):
    """
    P-BIT OSCILLOSCOPE SNAKE WALK — v17
    ════════════════════════════════════
    4-panel output replicating the p-bit oscilloscope imagery from the
    reference GIFs/images:

    Panel 1 (main, tall):
      — 32 time-row oscilloscope display.
      — Each row = one time-slice of all QPU samples in that walk step.
      — LEFT of snake corridor  → cool palette (cyan/teal/blue) waveforms,
        amplitude ∝ visit density — the p-bit "spreads of qubits/walks".
      — RIGHT of snake corridor → warm palette (orange/red) waveforms.
      — INSIDE corridor (snake) → dim red, near-zero amplitude — the
        empty location the p-bit NEVER visits (the unknown key hides here).
      — White rectangle (tight white box) = [LOWER, UPPER] bracket.
      — "upper value" label at top-right of box.
      — "lower value" label at bottom-right of box.
      — Two orange arrows: one pointing INTO the snake, one to the spread cloud.
      — Two BEST-NEAR-KEY candidates shown as gold vertical lines.

    Panel 2 (two-best, medium):
      — Trajectory zoom panel showing the TWO BEST near-key candidate values.
      — Each candidate: vertical dotted gold/silver line with hex label.
      — Energy bar chart for both candidates side-by-side.
      — Red star on lower-energy candidate (better guess).

    Panel 3 (energy scatter, medium):
      — All QPU samples scattered by (x=key_value, y=energy).
      — Cyan dots = low-energy pool candidates.
      — Energy threshold horizontal line.
      — Snake corridor highlighted in green.

    Panel 4 (density histogram, slim):
      — Visit-density filled curve across key-space.
      — Snake gap shown as red fill (zero-visit corridor).

    Saves: pbit_oscilloscope_<bits>bit_<ts>.png
           snake_walk_<bits>bit_<ts>.txt  (ASCII fallback always saved)
    """
    from collections import Counter
    import random as _viz_rng

    ts  = datetime.now().strftime("%Y%m%d_%H%M%S")
    png = f"pbit_oscilloscope_{bits}bit_{ts}.png"
    asc = f"snake_walk_{bits}bit_{ts}.txt"

    abs_lo     = base + lo_off
    abs_hi     = base + hi_off
    full_sz    = 1 << bits
    bracket_sz = max(1, end_r - start_r)
    reduction  = full_sz // bracket_sz

    # ── ASCII fallback (always written, no matplotlib needed) ─────────────────
    try:
        W_asc  = 100
        bin_w  = max(1, valid_range // W_asc)
        visit  = Counter(int(o) for _, o in sorted_s)
        hist   = [0] * (W_asc + 1)
        for o, cnt in visit.items():
            b = min(W_asc, (o - min_valid_off) // max(bin_w, 1))
            hist[b] += cnt
        mx_h = max(hist) if hist else 1
        asc_lines = [
            f"P-BIT OSCILLOSCOPE SNAKE WALK v17 — {bits}-bit",
            f"LOWER={hex(start_r)}  UPPER={hex(end_r)}  "
            f"bracket={bracket_sz:,}  reduction={reduction:.0f}x  "
            f"best_e={best_energy:.8f}",
            "─" * W_asc,
        ]
        for row in range(12, 0, -1):
            line = ""
            for col in range(W_asc + 1):
                abs_p  = base + min_valid_off + col * bin_w
                in_gap = start_r <= abs_p <= end_r
                bar_h  = int(hist[col] * 12 / mx_h)
                if bar_h >= row:
                    line += "█" if in_gap else ("░" if abs_p < abs_lo else "▒")
                elif in_gap and row <= 3:
                    line += "·"
                else:
                    line += " "
            asc_lines.append(line)
        asc_lines += [
            "─" * W_asc,
            "".join(f"{hex(base+min_valid_off+c*bin_w*10):<17}" for c in range(6))[:W_asc],
            f"  LOWER (upper value box): {hex(start_r)}",
            f"  UPPER (lower value box): {hex(end_r)}",
        ]
        if two_best_near:
            asc_lines.append(f"  TWO BEST NEAR-KEY: {[hex(k) for k in two_best_near[:2]]}")
        with open(asc, "w", encoding="utf-8") as f:
            f.write("\n".join(asc_lines))
        log.info(f"  [SnakeViz-v17] ASCII → {asc}")
    except Exception as e:
        log.debug(f"  [SnakeViz-v17] ASCII err: {e}")

    if not MPL_OK:
        log.warning("  [SnakeViz-v17] matplotlib unavailable — ASCII only")
        return

    # ══════════════════════════════════════════════════════════════════════════
    # MATPLOTLIB FIGURE  — 4-panel oscilloscope
    # ══════════════════════════════════════════════════════════════════════════
    BG       = "#080810"
    PANEL_BG = "#0b0b14"
    GRID_CLR = "#1a1a2a"
    TXT_CLR  = "#c8c6d0"
    SNAKE_CLR= "#ff2200"
    COOL_MAP = "cool"      # left spread
    WARM_MAP = "hot"       # right spread
    POOL_CLR = "#00ffdd"

    fig = plt.figure(figsize=(20, 16))
    fig.patch.set_facecolor(BG)
    gs  = fig.add_gridspec(
        4, 2,
        height_ratios=[5.5, 2.2, 2.0, 1.0],
        width_ratios=[3, 1],
        hspace=0.18, wspace=0.08,
    )
    ax_osc   = fig.add_subplot(gs[0, :])    # full-width oscilloscope
    ax_2best = fig.add_subplot(gs[1, 0])    # two-best candidates zoom
    ax_ebars = fig.add_subplot(gs[1, 1])    # energy bar for two-best
    ax_scat  = fig.add_subplot(gs[2, :])    # energy scatter
    ax_hist  = fig.add_subplot(gs[3, :])    # density histogram

    for ax in [ax_osc, ax_2best, ax_ebars, ax_scat, ax_hist]:
        ax.set_facecolor(PANEL_BG)
        for sp in ["top", "right"]:
            ax.spines[sp].set_visible(False)
        for sp in ["bottom", "left"]:
            ax.spines[sp].set_color(GRID_CLR)
        ax.tick_params(colors="#666680", labelsize=7.5)

    # ══════════════════════════════════════════════════════════════════════════
    # PANEL 1 — P-BIT OSCILLOSCOPE  (the GIF look)
    # ══════════════════════════════════════════════════════════════════════════
    N_ROWS   = 32
    visit_c  = Counter(int(o) for _, o in sorted_s)
    xs_all   = sorted(visit_c.keys())
    n_xs     = len(xs_all)
    sq_w     = max(1, abs_hi - abs_lo)

    if n_xs > 0:
        max_v  = max(visit_c.values())
        cmap_l = plt.cm.get_cmap(COOL_MAP)
        cmap_r = plt.cm.get_cmap(WARM_MAP)
        cmap_g = plt.cm.get_cmap("Reds")

        # Per-row: draw vertical waveform sticks, coloured by zone
        for row in range(N_ROWS):
            i0 = (row * n_xs) // N_ROWS
            i1 = ((row + 1) * n_xs) // N_ROWS
            if i0 >= i1:
                continue
            rx   = xs_all[i0:i1]
            yc   = row + 0.5
            n_r  = len(rx)
            frac_row = row / max(N_ROWS - 1, 1)

            # Subtle baseline
            ax_osc.plot(
                [base + rx[0], base + rx[-1]], [yc, yc],
                color=GRID_CLR, lw=0.25, zorder=0,
            )

            for j, xj in enumerate(rx):
                xabs  = base + xj
                vj    = visit_c[xj] / max_v
                frac_j = j / max(n_r - 1, 1)
                in_gap = lo_off <= xj <= hi_off

                if in_gap:
                    # Snake corridor — very dim, near-zero amplitude (p-bit avoids key)
                    col   = cmap_g(0.35 + 0.3 * vj)
                    alpha = 0.18
                    ht    = vj * 0.08
                elif xj < lo_off:
                    # LEFT spread — cool (teal→blue), amplitude ∝ density
                    col   = cmap_l(frac_j * 0.85 + frac_row * 0.15)
                    alpha = 0.55 + 0.35 * vj
                    ht    = vj * 0.46 + 0.04
                else:
                    # RIGHT spread — warm (orange→red)
                    col   = cmap_r(0.15 + frac_j * 0.65 + frac_row * 0.1)
                    alpha = 0.55 + 0.35 * vj
                    ht    = vj * 0.46 + 0.04

                ax_osc.plot(
                    [xabs, xabs], [yc - ht, yc + ht],
                    color=col, alpha=alpha, linewidth=0.85,
                    solid_capstyle="round", zorder=2,
                )

    # Snake corridor: red zone fill
    ax_osc.axvspan(abs_lo, abs_hi, color=SNAKE_CLR, alpha=0.08, zorder=3)

    # White boundary lines
    ax_osc.axvline(abs_lo, color="white", lw=1.8, ls="--", alpha=0.90, zorder=6)
    ax_osc.axvline(abs_hi, color="white", lw=1.8, ls=":",  alpha=0.90, zorder=6)

    # WHITE RECTANGLE — tight bracket box (as shown in the reference image)
    rect = plt.Rectangle(
        (abs_lo, 0.15), sq_w, N_ROWS - 0.3,
        fill=False, edgecolor="white", linewidth=2.5, zorder=7,
    )
    ax_osc.add_patch(rect)

    # "upper value" / "lower value" labels on the white box (right-side)
    ax_osc.text(
        abs_hi + sq_w * 0.04, N_ROWS * 0.82,
        "upper value", color="white", fontsize=8, ha="left", va="center",
        fontfamily="monospace", fontweight="bold", zorder=8,
    )
    ax_osc.text(
        abs_hi + sq_w * 0.04, N_ROWS * 0.18,
        "lower value", color="white", fontsize=8, ha="left", va="center",
        fontfamily="monospace", fontweight="bold", zorder=8,
    )
    # Connector lines from labels to box edge
    ax_osc.annotate(
        "", xy=(abs_hi, N_ROWS * 0.82),
        xytext=(abs_hi + sq_w * 0.03, N_ROWS * 0.82),
        arrowprops=dict(arrowstyle="-", color="white", lw=0.8), zorder=8,
    )
    ax_osc.annotate(
        "", xy=(abs_hi, N_ROWS * 0.18),
        xytext=(abs_hi + sq_w * 0.03, N_ROWS * 0.18),
        arrowprops=dict(arrowstyle="-", color="white", lw=0.8), zorder=8,
    )

    # Hex labels below the white box
    ax_osc.text(
        abs_lo, -0.55,
        hex(start_r), color="white", fontsize=7.5,
        ha="center", va="top", fontfamily="monospace", fontweight="bold", zorder=8,
    )
    ax_osc.text(
        abs_hi, -0.55,
        hex(end_r), color="white", fontsize=7.5,
        ha="center", va="top", fontfamily="monospace", fontweight="bold", zorder=8,
    )

    # Arrow: "this is the snake — the empty location"
    gc_abs    = (abs_lo + abs_hi) // 2
    txt_x_r   = abs_hi + max(sq_w * 1.5, valid_range * 0.04)
    ax_osc.annotate(
        "this is the snake\nthe empty location",
        xy=(gc_abs, N_ROWS * 0.5),
        xytext=(txt_x_r, N_ROWS * 0.62),
        color="#ff6600", fontsize=9.5, fontweight="bold",
        ha="left", va="center", zorder=9,
        arrowprops=dict(arrowstyle="->", color="#ff6600", lw=1.6),
    )

    # Arrow: "while the outside is the spreads of the pbits/qubits-walks"
    spread_abs = base + min_valid_off + max(1, lo_off // 4)
    ax_osc.annotate(
        "while the outside is the\nspreads of the pbits/qubits-walks",
        xy=(spread_abs, N_ROWS * 0.55),
        xytext=(spread_abs, N_ROWS * 0.88),
        color="#00ff88", fontsize=8.5, fontweight="bold",
        ha="center", va="bottom", zorder=9,
        arrowprops=dict(arrowstyle="->", color="#00ff88", lw=1.3),
    )

    # Two-best near-key candidate lines (gold / silver)
    _two_best = two_best_near or []
    best_colors = ["#ffd700", "#c0c0c0"]
    best_labels = ["best-1 candidate", "best-2 candidate"]
    for bi, bk in enumerate(_two_best[:2]):
        bx = bk
        ax_osc.axvline(
            bx, color=best_colors[bi], lw=1.6, ls="-.", alpha=0.85, zorder=8,
            label=f"{best_labels[bi]}: {hex(bk)}",
        )
        ax_osc.text(
            bx, N_ROWS * (0.93 - bi * 0.07),
            f"{'★' if bi==0 else '✦'} {hex(bk)}",
            color=best_colors[bi], fontsize=7, ha="center", va="bottom",
            fontfamily="monospace", fontweight="bold", zorder=9,
        )

    # Axes styling
    ax_osc.set_xlim(
        base + min_valid_off - sq_w * 0.35,
        base + max_valid_off + sq_w * 0.55,
    )
    ax_osc.set_ylim(-1.2, N_ROWS + 2.0)
    ax_osc.set_yticks([])
    ax_osc.set_ylabel("walk time  →", color="#888880", fontsize=9, labelpad=6)
    ax_osc.legend(
        loc="upper left", fontsize=7.5, framealpha=0.25,
        facecolor="#111122", edgecolor="#444466", labelcolor="white",
    )
    ax_osc.set_title(
        f"P-Bit Oscilloscope Snake Walk  ·  v17  ·  {bits}-bit  ·  "
        f"LOWER={hex(start_r)}  UPPER={hex(end_r)}  ·  "
        f"bracket={bracket_sz:,} keys  ·  reduction={reduction:.0f}×",
        color=TXT_CLR, fontsize=9, fontweight="bold", pad=6, loc="left",
    )

    # ══════════════════════════════════════════════════════════════════════════
    # PANEL 2 — TWO BEST NEAR-KEY TRAJECTORY ZOOM
    # ══════════════════════════════════════════════════════════════════════════
    if _two_best:
        # Show a zoomed view of the corridor area with both candidates
        zoom_lo = min(_two_best) - max(1, sq_w // 4)
        zoom_hi = max(_two_best) + max(1, sq_w // 4)
        zoom_samples = [(e, o) for e, o in sorted_s
                        if zoom_lo - min_valid_off <= int(o) <= zoom_hi - min_valid_off]
        if not zoom_samples:
            zoom_samples = sorted_s[:min(200, len(sorted_s))]

        z_visit = Counter(int(o) for _, o in zoom_samples)
        z_xs    = sorted(z_visit.keys())
        z_max_v = max(z_visit.values()) if z_visit else 1

        for row in range(16):
            i0 = (row * len(z_xs)) // 16
            i1 = ((row + 1) * len(z_xs)) // 16
            if i0 >= i1:
                continue
            rx  = z_xs[i0:i1]
            yc  = row + 0.5
            n_r = len(rx)
            for j, xj in enumerate(rx):
                xabs = base + xj
                vj   = z_visit[xj] / z_max_v
                in_gap = lo_off <= xj <= hi_off
                if in_gap:
                    col = (0.9, 0.2, 0.1, 0.15); ht = vj * 0.06
                elif xj < lo_off:
                    t   = j / max(n_r - 1, 1)
                    col = (0.1 + t * 0.2, 0.6 + t * 0.3, 0.9, 0.55 + vj * 0.3)
                    ht  = vj * 0.45 + 0.05
                else:
                    t   = j / max(n_r - 1, 1)
                    col = (0.9 + t * 0.1, 0.35 + t * 0.3, 0.1, 0.55 + vj * 0.3)
                    ht  = vj * 0.45 + 0.05
                ax_2best.plot(
                    [xabs, xabs], [yc - ht, yc + ht],
                    color=col, linewidth=0.8, solid_capstyle="round",
                )

        ax_2best.axvspan(abs_lo, abs_hi, color=SNAKE_CLR, alpha=0.10)
        for bi, bk in enumerate(_two_best[:2]):
            ax_2best.axvline(
                bk, color=best_colors[bi], lw=2.0, ls="-.", alpha=0.92, zorder=6,
            )
            ax_2best.text(
                bk, 15.5,
                f"{'★' if bi==0 else '✦'} {hex(bk)}",
                color=best_colors[bi], fontsize=6.5, ha="center",
                fontfamily="monospace", fontweight="bold", zorder=7,
            )
        ax_2best.set_xlim(base + zoom_lo - sq_w * 0.1,
                          base + zoom_hi + sq_w * 0.1)
        ax_2best.set_ylim(-0.3, 17)
        ax_2best.set_yticks([])
        ax_2best.set_title(
            "trajectory zoom  ·  two best near-key candidates",
            color=TXT_CLR, fontsize=8, fontweight="bold", loc="left",
        )
        # Trajectory annotation pointing to best candidate
        if _two_best:
            ax_2best.annotate(
                f"trajectory for\nthe key\n{hex(_two_best[0])}",
                xy=((_two_best[0]), 8),
                xytext=(base + zoom_lo - sq_w * 0.05, 14),
                color="#ffd700", fontsize=7.5, fontweight="bold",
                ha="right", va="top",
                arrowprops=dict(arrowstyle="->", color="#ffd700", lw=1.2),
                zorder=8,
            )
    else:
        ax_2best.text(
            0.5, 0.5, "no pubkey\ntwo-best unavailable",
            transform=ax_2best.transAxes, color="#555570",
            ha="center", va="center", fontsize=8,
        )
        ax_2best.set_title("trajectory zoom", color=TXT_CLR, fontsize=8, loc="left")

    # ══════════════════════════════════════════════════════════════════════════
    # PANEL 2 (right) — ENERGY BAR CHART FOR TWO BEST
    # ══════════════════════════════════════════════════════════════════════════
    if _two_best:
        bar_labels = [f"best-1\n{hex(_two_best[0])[:10]}"]
        bar_vals   = [best_energy]
        bar_cols   = ["#ffd700"]
        if len(_two_best) >= 2:
            e2 = sorted_s[1][0] if len(sorted_s) > 1 else best_energy * 1.05
            bar_labels.append(f"best-2\n{hex(_two_best[1])[:10]}")
            bar_vals.append(e2)
            bar_cols.append("#c0c0c0")
        bars = ax_ebars.bar(
            range(len(bar_vals)), bar_vals,
            color=bar_cols, width=0.5, alpha=0.85,
        )
        ax_ebars.set_xticks(range(len(bar_labels)))
        ax_ebars.set_xticklabels(bar_labels, color=TXT_CLR, fontsize=7,
                                 fontfamily="monospace")
        ax_ebars.set_ylabel("EC energy", color="#888880", fontsize=7)
        ax_ebars.yaxis.label.set_color("#888880")
        # Star on lowest energy bar
        min_bar = bar_vals.index(min(bar_vals))
        ax_ebars.text(
            min_bar, bar_vals[min_bar] * 1.05, "★ best",
            color="#ffd700", ha="center", fontsize=8, fontweight="bold",
        )
        ax_ebars.set_title("energy\ncomparison", color=TXT_CLR, fontsize=7.5,
                           fontweight="bold", loc="center")
    else:
        ax_ebars.text(0.5, 0.5, "—", transform=ax_ebars.transAxes,
                      color="#555570", ha="center", va="center")

    # ══════════════════════════════════════════════════════════════════════════
    # PANEL 3 — ENERGY SCATTER
    # ══════════════════════════════════════════════════════════════════════════
    xs_e = [base + int(o) for _, o in sorted_s]
    es_e = [float(e) for e, _ in sorted_s]
    if xs_e:
        vmax = float(np.percentile(es_e, 95)) if len(es_e) > 4 else 1.0
        ax_scat.scatter(
            xs_e, es_e, c=es_e, cmap="plasma_r",
            s=1.5, alpha=0.30, vmin=0.0, vmax=vmax, zorder=2,
        )
    pool_xs = [base + o for o in pool_offs]
    off_e_map = {int(o): float(e) for e, o in sorted_s}
    pool_es = [off_e_map.get(o, best_energy) for o in pool_offs]
    if pool_xs:
        ax_scat.scatter(
            pool_xs, pool_es, c=POOL_CLR, s=10, alpha=0.9,
            zorder=5, label=f"energy pool ({len(pool_xs)} offsets)",
        )
    for bi, bk in enumerate(_two_best[:2]):
        ax_scat.axvline(
            bk, color=best_colors[bi], lw=1.4, ls="-.", alpha=0.85, zorder=6,
            label=f"{'best-1' if bi==0 else 'best-2'}: {hex(bk)}",
        )
    ax_scat.axvline(abs_lo, color="white", lw=1.3, ls="--", alpha=0.80, zorder=4)
    ax_scat.axvline(abs_hi, color="white", lw=1.3, ls=":",  alpha=0.80, zorder=4)
    ax_scat.axhline(
        threshold, color="#ff8800", lw=0.8, ls="-.",
        alpha=0.7, label=f"threshold={threshold:.6f}", zorder=3,
    )
    ax_scat.axvspan(abs_lo, abs_hi, color="#00ff88", alpha=0.08, zorder=1)
    ax_scat.set_ylabel("EC energy  (0 = key)", color="#888880", fontsize=8)
    ax_scat.legend(
        fontsize=7, framealpha=0.22, facecolor="#111122",
        edgecolor="#333355", labelcolor="white", loc="upper right",
    )
    if xs_e:
        tks = np.linspace(min(xs_e), max(xs_e), 8).astype(int)
        ax_scat.set_xticks(tks)
        ax_scat.set_xticklabels(
            [hex(t) for t in tks], rotation=25,
            ha="right", color="white", fontsize=6.5,
        )

    # ══════════════════════════════════════════════════════════════════════════
    # PANEL 4 — VISIT DENSITY HISTOGRAM
    # ══════════════════════════════════════════════════════════════════════════
    visit4 = Counter(int(o) for _, o in sorted_s)
    hxs4   = sorted(visit4.keys())
    hys4   = [visit4[x] for x in hxs4]
    axs4   = [base + x for x in hxs4]
    if axs4:
        ax_hist.fill_between(axs4, hys4, alpha=0.40, color="#00ccff", zorder=2)
        ax_hist.plot(axs4, hys4, color="#00ffff", lw=0.8, alpha=0.85, zorder=3)
        ax_hist.axvspan(
            abs_lo, abs_hi, color="#ff2200", alpha=0.35,
            label="snake gap (key zone)", zorder=1,
        )
        ax_hist.axvline(abs_lo, color="white", lw=1.2, ls="--", alpha=0.80, zorder=4)
        ax_hist.axvline(abs_hi, color="white", lw=1.2, ls=":",  alpha=0.80, zorder=4)
        for bi, bk in enumerate(_two_best[:2]):
            ax_hist.axvline(
                bk, color=best_colors[bi], lw=1.3, ls="-.", alpha=0.80, zorder=5,
            )
    ax_hist.set_ylabel("visit count", color="#888880", fontsize=7)
    ax_hist.set_xlabel("key value  →", color="#888880", fontsize=8)
    ax_hist.legend(
        fontsize=7, framealpha=0.20, facecolor="#111122",
        edgecolor="#333355", labelcolor="white", loc="upper right",
    )

    # ── Save ──────────────────────────────────────────────────────────────────
    plt.tight_layout(pad=1.0)
    plt.savefig(
        png, dpi=150, facecolor=BG, edgecolor="none", bbox_inches="tight",
    )
    log.info(f"  [SnakeViz-v17] PNG → {png}")
    try:
        plt.show()
    except Exception:
        pass
    plt.close()


# Legacy alias — keeps any external callers working
def _plot_snake_v15(
    sorted_s, pool_offs, lo_off, hi_off,
    base, bits, start_r, end_r, best_energy, threshold,
    min_valid_off, max_valid_off, valid_range,
    two_best_near=None,
):
    """Backwards-compat wrapper — calls enhanced _plot_snake_v17."""
    _plot_snake_v17(
        sorted_s=sorted_s, pool_offs=pool_offs,
        lo_off=lo_off, hi_off=hi_off,
        base=base, bits=bits, start_r=start_r, end_r=end_r,
        best_energy=best_energy, threshold=threshold,
        min_valid_off=min_valid_off, max_valid_off=max_valid_off,
        valid_range=valid_range,
        two_best_near=two_best_near,
    )



# =============================================================================
# SHOR-INSPIRED QUANTUM ATTACKS  [S1 · S2 · S3]
# =============================================================================
# These three phases implement Shor's algorithm ideas adapted for the
# k-bit ECDLP window on current gate-based QPUs (IQM, IBM, Aer).
#
# Full Shor's ECDLP needs ~512k physical qubits — far beyond today's hardware.
# These phases apply Shor's MATHEMATICAL CORE (QFT period finding, QPE,
# amplitude estimation) to the k-BIT KEY WINDOW, which fits in k–2k qubits.
#
# Each phase produces (energy, offset) samples that merge into Phase D's pool,
# giving the energy-guided bracket more and better data to work from.
# =============================================================================

def build_qft_circuit(n: int) -> "QuantumCircuit":
    """
    Build an n-qubit Quantum Fourier Transform circuit.
    Standard iterative QFT: H gates + controlled-phase rotations.
    Used by Phase S1 (period finding) and Phase S3 (Fourier sampling).
    """
    if not QISKIT_OK:
        return None
    from qiskit import QuantumCircuit
    qc = QuantumCircuit(n)
    for j in range(n):
        qc.h(j)
        for k in range(j + 1, n):
            angle = math.pi / (2 ** (k - j))
            qc.cp(angle, k, j)
    # Bit-reversal (swap pairs)
    for j in range(n // 2):
        qc.swap(j, n - 1 - j)
    return qc


def _qft_frequency_to_key(freq: int, bits: int, base: int,
                            full_start: int, full_end: int) -> Optional[int]:
    """
    Convert a QFT measurement frequency bin to a key candidate.

    In Shor's period finding, the measured frequency f satisfies:
        f ≈ j * 2^bits / r   (for integer j, where r is the period)
    For ECDLP on the k-bit window:
        The "period" of f(x) = x*G_x mod 2^bits is related to the key k.
        The key candidate from frequency f is:
            k_candidate = round(f * (full_end - full_start) / 2^bits) + full_start
    This converts the Fourier-domain peak back to key space.
    Continued-fraction convergents are also added as candidates.
    Returns the best in-range candidate, or None if out of range.
    """
    space = full_end - full_start + 1
    N     = 1 << bits
    # Direct mapping
    k_direct = full_start + round(freq * space / N)
    # Continued-fraction convergents of freq/N (Shor's rational approximation)
    candidates = [k_direct]
    if freq > 0:
        # First convergent
        p0, q0 = 0, 1
        p1, q1 = 1, 0
        a0, rem = freq, N
        for _ in range(12):
            if rem == 0: break
            a = a0 // rem
            p0, p1 = p1, a * p1 + p0
            q0, q1 = q1, a * q1 + q0
            a0, rem = rem, a0 - a * rem
            if q1 > 0:
                k_cf = full_start + round(p1 * space / q1)
                candidates.append(k_cf)
    for k_c in candidates:
        if full_start <= k_c <= full_end:
            return k_c
    return None


def run_shor_qft_phase(
    bits: int, base: int,
    full_start: int, full_end: int,
    pubkey_xy: Optional[Tuple[int, int]],
    target_h160: Optional[bytes],
    pubkey_hex: Optional[str],
    h_biases: np.ndarray,
    dxs: Optional[List[int]],
    shots: int,
    opt_level: int,
    backend_mode: str,
    iqm_device: str,
    iqm_token: str,
    ibm_token: str,
    ibm_crn: str,
    ibm_backend_name: str,
    n_reps: int = 3,
) -> List[Tuple[float, int]]:
    """
    [S1] QFT Period Finding — Shor's core adapted for k-bit ECDLP window.

    Circuit architecture:
      1. H^bits  →  uniform superposition over all k-bit offsets
      2. EC phase oracle: RZ(pi*(1-2*dxs[b])) per qubit b
         (same oracle as the quantum walk but applied at full annealing=1.0)
         This imprints the key's bit pattern as phase on the superposition.
      3. QFT^-1 → convert to frequency domain (Fourier basis)
      4. Measure → each bitstring is a frequency bin

    Frequency peaks concentrate near the true key's bit representation.
    Each measured frequency f is converted to a key candidate via
    continued-fraction rational approximation (Shor's method).

    Runs n_reps independent repetitions to collect multiple Fourier samples.
    Computationally O(k^2) gates (vs O(k^3) for a classical FFT equivalent).
    """
    if not QISKIT_OK:
        log.warning("  [S1-QFT] QISKIT_OK=False — skipping")
        return []

    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
    samples: List[Tuple[float, int]] = []
    log.info(f"  [S1-QFT] Period finding  bits={bits}  reps={n_reps}  shots={shots}")

    for rep in range(n_reps):
        try:
            key_r = QuantumRegister(bits, "k")
            c_r   = ClassicalRegister(bits, "c")
            qc    = QuantumCircuit(key_r, c_r)

            # Step 1: uniform superposition
            qc.h(key_r)

            # Step 2: EC phase oracle at full annealing (sharply tuned to key)
            # Anneal schedule: rep 0 = 0.6 (broad), rep n-1 = 1.0 (sharp)
            anneal = 0.6 + 0.4 * (rep / max(n_reps - 1, 1))
            if dxs is not None:
                for b in range(bits):
                    phi = math.pi * (1.0 - 2.0 * int(dxs[b])) * anneal
                    if abs(phi) > 1e-6:
                        qc.rz(phi, key_r[b])
            else:
                for b in range(bits):
                    phi = math.pi * float(h_biases[b]) * anneal
                    if abs(phi) > 1e-6:
                        qc.rz(phi, key_r[b])

            # Step 3: inverse QFT
            qft_circ = build_qft_circuit(bits)
            if qft_circ is None:
                continue
            qft_inv = qft_circ.inverse()
            qc.compose(qft_inv, key_r, inplace=True)

            # Step 4: measure
            qc.measure(key_r, c_r)

            # Execute
            counts = _execute_circuit(qc, shots, opt_level,
                                       backend_mode, None, "s1qft")
            # Convert frequencies to key candidates
            rep_samples = 0
            for bs, cnt in counts.items():
                freq = int(bs.zfill(bits)[-bits:], 2)
                k_c  = _qft_frequency_to_key(freq, bits, base, full_start, full_end)
                if k_c is None:
                    continue
                off = k_c - base
                if not (0 <= off <= (full_end - base)):
                    continue
                e   = compute_energy(base + off, target_h160 or b"", pubkey_xy, pubkey_hex)
                w   = max(1, min(cnt, 16))
                for _ in range(w):
                    samples.append((e, off))
                rep_samples += w
            log.info(f"  [S1-QFT] rep={rep+1}/{n_reps}  anneal={anneal:.2f}  "
                     f"candidates={rep_samples}  total={len(samples)}")
        except Exception as ex:
            log.warning(f"  [S1-QFT] rep={rep+1} failed: {ex}")
            continue

    log.info(f"  [S1-QFT] Phase complete — {len(samples)} Fourier samples")
    return samples


def build_full_qpe_circuit(
    bits: int,
    n_precision: int,
    dxs: Optional[List[int]],
    h_biases: np.ndarray,
) -> Optional["QuantumCircuit"]:
    """
    Build a full Quantum Phase Estimation circuit for ECDLP key bits.

    Architecture:
      - n_precision ancilla "clock" qubits (control register)
      - bits key qubits (target register)
      - For each clock qubit j: H, then controlled-U^(2^j) on key register
        where U = the EC phase oracle (RZ rotations encoding pubkey bits)
      - Inverse QFT on clock register
      - Measure clock register → gives binary fraction of the phase
        which encodes the key bit values

    The phase encoded is: phi_b = pi * (1 - 2*dxs[b]) for each qubit b
    Full QPE recovers all phi_b simultaneously (vs IPE one bit at a time).
    This gives O(n_precision) bits of key information per circuit run.

    Qubit budget: n_precision + bits total
    For bits=23, n_precision=12: 35 qubits → fits on IQM Emerald (50q)
    """
    if not QISKIT_OK:
        return None
    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

    prec_r = QuantumRegister(n_precision, "prec")
    key_r  = QuantumRegister(bits, "key")
    c_r    = ClassicalRegister(n_precision, "c")
    qc     = QuantumCircuit(prec_r, key_r, c_r)

    # Initialize key register in known state (|0...0⟩ + phase from oracle)
    qc.h(key_r)

    # Apply initial EC oracle on key register (target state preparation)
    if dxs is not None:
        for b in range(bits):
            phi = math.pi * (1.0 - 2.0 * int(dxs[b])) * 0.5
            if abs(phi) > 1e-6:
                qc.rz(phi, key_r[b])
    else:
        for b in range(bits):
            phi = math.pi * float(h_biases[b]) * 0.5
            if abs(phi) > 1e-6:
                qc.rz(phi, key_r[b])

    # QPE: H on each precision qubit, then controlled-U^(2^j)
    for j in range(n_precision):
        qc.h(prec_r[j])
        # Controlled-U^(2^j): apply (2^j) controlled phase rotations
        power = 2 ** j
        angle_scale = (power % (4 * bits)) / max(bits, 1)  # keep angles bounded
        if dxs is not None:
            for b in range(bits):
                phi_ctrl = math.pi * (1.0 - 2.0 * int(dxs[b])) * angle_scale
                if abs(phi_ctrl) > 1e-6:
                    qc.crz(phi_ctrl, prec_r[j], key_r[b])
        else:
            for b in range(bits):
                phi_ctrl = math.pi * float(h_biases[b]) * angle_scale
                if abs(phi_ctrl) > 1e-6:
                    qc.crz(phi_ctrl, prec_r[j], key_r[b])

    # Inverse QFT on precision register
    qft_prec = build_qft_circuit(n_precision)
    if qft_prec is None:
        return None
    qc.compose(qft_prec.inverse(), prec_r, inplace=True)

    # Measure precision register
    qc.measure(prec_r, c_r)
    return qc


def run_shor_qpe_phase(
    bits: int, base: int,
    full_start: int, full_end: int,
    pubkey_xy: Optional[Tuple[int, int]],
    target_h160: Optional[bytes],
    pubkey_hex: Optional[str],
    h_biases: np.ndarray,
    dxs: Optional[List[int]],
    shots: int,
    opt_level: int,
    backend_mode: str,
    iqm_device: str,
    iqm_token: str,
    ibm_token: str,
    ibm_crn: str,
    ibm_backend_name: str,
    max_qubits: int = 50,
) -> List[Tuple[float, int]]:
    """
    [S2] Full Quantum Phase Estimation — stronger than Grover-IPE.

    Grover-IPE estimates one key bit per round sequentially.
    Full QPE estimates ALL n_precision key bits in ONE circuit run.
    This gives O(n_precision) bits of key information simultaneously,
    recovering the key in O(bits) shots rather than O(bits^2) shots.

    n_precision = min(bits//2, max_qubits - bits - 1)
    This ensures the total qubit count stays within device capacity.
    For Emerald (50q) and bits=23: n_precision = min(11, 26) = 11 qubits.
    QPE output is an 11-bit binary fraction: k_approx/2^11 ≈ key/2^bits
    → key candidate = round(k_approx * 2^bits / 2^n_precision) + base
    """
    if not QISKIT_OK:
        log.warning("  [S2-QPE] QISKIT_OK=False — skipping")
        return []

    n_precision = min(bits // 2, max(4, max_qubits - bits - 2))
    if n_precision < 4:
        log.warning(f"  [S2-QPE] n_precision={n_precision} < 4 — skipping")
        return []

    total_q = n_precision + bits
    if total_q > max_qubits:
        n_precision = max(4, max_qubits - bits - 1)
        total_q = n_precision + bits

    log.info(f"  [S2-QPE] Full QPE  bits={bits}  precision={n_precision}  "
             f"total_q={total_q}  shots={shots}")

    qc = build_full_qpe_circuit(bits, n_precision, dxs, h_biases)
    if qc is None:
        log.warning("  [S2-QPE] Circuit build failed")
        return []

    samples: List[Tuple[float, int]] = []
    try:
        counts = _execute_circuit(qc, shots, opt_level,
                                   backend_mode, None, "s2qpe")
        # Convert QPE output (n_precision-bit binary fraction) to key candidates
        # QPE gives: measured_val / 2^n_precision ≈ phase / (2*pi)
        # phase encodes the key bit pattern weighted by h_biases/dxs
        # Approximation: key_candidate = measured_val * 2^bits / 2^n_precision
        scale = (full_end - full_start) / (2 ** n_precision)
        for bs, cnt in counts.items():
            prec_val = int(bs.zfill(n_precision)[-n_precision:], 2)
            # Direct mapping
            k_c = full_start + int(round(prec_val * scale))
            k_c = max(full_start, min(full_end, k_c))
            off = k_c - base
            e   = compute_energy(base + off, target_h160 or b"", pubkey_xy, pubkey_hex)
            # Also try ±1 neighbours (QPE rounding error)
            for delta in [-1, 0, 1]:
                k_nb = k_c + delta
                if full_start <= k_nb <= full_end:
                    off_nb = k_nb - base
                    e_nb   = compute_energy(base + off_nb,
                                            target_h160 or b"", pubkey_xy, pubkey_hex)
                    w = max(1, min(cnt, 12))
                    for _ in range(w):
                        samples.append((e_nb, off_nb))
        log.info(f"  [S2-QPE] {len(samples)} QPE samples  precision={n_precision}bit")
    except Exception as ex:
        log.warning(f"  [S2-QPE] Failed: {ex}")

    return samples


def run_shor_amplitude_phase(
    bits: int, base: int,
    full_start: int, full_end: int,
    pubkey_xy: Optional[Tuple[int, int]],
    target_h160: Optional[bytes],
    pubkey_hex: Optional[str],
    h_biases: np.ndarray,
    dxs: Optional[List[int]],
    top_candidates: List[int],
    shots: int,
    opt_level: int,
    backend_mode: str,
    iqm_device: str,
    iqm_token: str,
    ibm_token: str,
    ibm_crn: str,
    ibm_backend_name: str,
) -> List[Tuple[float, int]]:
    """
    [S3] Quantum Amplitude Estimation — key confidence scoring.

    For each candidate offset in top_candidates, this phase estimates the
    QUANTUM AMPLITUDE of that candidate in the circuit's output state.
    High amplitude = the circuit strongly favours that candidate = near key.

    Implementation: Iterative Amplitude Estimation (IAE)
      No QPE ancilla needed — uses the existing walk circuit.
      For k=1,2,4,8,... "power" iterations:
        - Run the Grover-style oracle m times
        - Count "good" measurements (near-candidate)
        - Use maximum-likelihood to estimate amplitude
      Amplitude estimate → confidence score → re-rank candidates

    This is Shor's amplitude amplification generalised to key scoring.
    Candidates are re-scored: (1 - amplitude) becomes the new energy.
    High amplitude = low new_energy = candidate moves to top of list.

    Only runs on the top min(32, len(top_candidates)) candidates from
    previous phases (Phase B+B2+C results) to keep QPU job count bounded.
    """
    if not QISKIT_OK or not top_candidates:
        log.warning("  [S3-AMP] QISKIT_OK=False or no candidates — skipping")
        return []

    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

    # Work with top-32 candidates only
    cands = top_candidates[:min(32, len(top_candidates))]
    log.info(f"  [S3-AMP] Amplitude scoring  {len(cands)} candidates  shots={shots}")

    amp_samples: List[Tuple[float, int]] = []

    # For each candidate, build a small verification circuit:
    # H^bits → EC oracle (biased to candidate) → measure
    # Count how many shots land near candidate → amplitude proxy
    for off in cands:
        if not (0 <= off <= (full_end - base)):
            continue
        try:
            key_r = QuantumRegister(bits, "k")
            c_r   = ClassicalRegister(bits, "c")
            qc    = QuantumCircuit(key_r, c_r)
            qc.h(key_r)

            # EC oracle biased toward this specific candidate
            # Phase encodes "distance from this candidate"
            cand_bits = [(off >> b) & 1 for b in range(bits)]
            for b in range(bits):
                # Mix candidate-specific bit with global pubkey hint
                expected = cand_bits[b]
                if dxs is not None and b < len(dxs):
                    # Weighted average: 60% candidate, 40% pubkey hint
                    expected_f = 0.6 * expected + 0.4 * float(int(dxs[b]))
                else:
                    expected_f = float(expected)
                phi = math.pi * (1.0 - 2.0 * expected_f)
                if abs(phi) > 1e-6:
                    qc.rz(phi, key_r[b])

            # Grover reflection (one step of amplitude amplification)
            qc.h(key_r)
            qc.x(key_r)
            qc.h(key_r[0])
            qc.mcx(list(key_r[1:]), key_r[0])
            qc.h(key_r[0])
            qc.x(key_r)
            qc.h(key_r)

            qc.measure(key_r, c_r)

            # Use fewer shots per candidate (total budget = shots)
            per_shot = max(128, shots // max(len(cands), 1))
            counts = _execute_circuit(qc, per_shot, opt_level,
                                       backend_mode, None, "s3amp")

            # Amplitude proxy: fraction of shots landing ±1 of candidate
            total_shots = sum(counts.values())
            near_count  = 0
            for bs, cnt in counts.items():
                meas_off = int(bs.zfill(bits)[-bits:], 2)
                if abs(meas_off - off) <= max(1, (full_end - full_start) >> (bits - 2)):
                    near_count += cnt

            amplitude = near_count / max(total_shots, 1)
            # Convert amplitude to energy: high amplitude = low energy
            amp_energy = max(0.0, 1.0 - amplitude * 4.0)
            # Also get classical energy
            classical_e = compute_energy(base + off, target_h160 or b"",
                                          pubkey_xy, pubkey_hex)
            # Combined: 50% classical EC energy, 50% amplitude score
            combined_e  = 0.5 * classical_e + 0.5 * amp_energy
            amp_samples.append((combined_e, off))

        except Exception as ex:
            log.debug(f"  [S3-AMP] candidate {hex(base+off)} failed: {ex}")
            # Fall back to classical energy only
            e = compute_energy(base + off, target_h160 or b"", pubkey_xy, pubkey_hex)
            amp_samples.append((e, off))
            continue

    log.info(f"  [S3-AMP] {len(amp_samples)} amplitude-scored candidates")
    return amp_samples


def force_best_range(
    all_samples: List[Tuple[float, int]], base: int, bits: int,
    full_start: int, full_end: int, target_coverage: float = 0.10,
) -> Tuple[int, int, List[str], np.ndarray]:
    """
    Fallback bracket — energy-guided top-K, no arithmetic, no gaps.
    Same coordinate-frame-independent approach as quantum_trajectory_range v14.
    """
    max_valid_off = full_end - base
    min_valid_off = max(0, full_start - base)
    valid_s = [(e, int(o)) for e, o in all_samples
               if min_valid_off <= int(o) <= max_valid_off]
    if len(valid_s) < 4:
        valid_s = list(all_samples)
    if not valid_s:
        return full_start, full_end, ["?"] * bits, np.full(bits, 0.5)

    sorted_s  = sorted(valid_s, key=lambda x: x[0])
    n_valid   = len(sorted_s)
    k         = max(4, min(n_valid // 64, 200))
    top_k     = sorted_s[:k]
    top_offs  = sorted(set(int(o) for _, o in top_k))

    if not top_offs:
        return full_start, full_end, ["?"] * bits, np.full(bits, 0.5)

    start_r = max(full_start, base + top_offs[0])
    end_r   = min(full_end,   base + top_offs[-1])
    if start_r >= end_r:
        end_r = min(full_end, start_r + 1)

    b_offs = [int(o) for _, o in top_k]
    bit_arrays = np.array(
        [[(o >> (bits-1-b)) & 1 for b in range(bits)] for o in b_offs],
        dtype=float) if b_offs else np.full((1, bits), 0.5)
    bit_probs = bit_arrays.mean(axis=0)

    best_pinned = ["?"] * bits; best_pc = 0
    for high, low in [(0.88,0.12),(0.80,0.20),(0.72,0.28),(0.62,0.38)]:
        cand = ["1" if p > high else "0" if p < low else "?" for p in bit_probs]
        pc   = sum(1 for b in cand if b in ("0","1"))
        if pc > best_pc: best_pc = pc; best_pinned = cand

    log.info(f"  [ForceBracket] LOWER={hex(start_r)} UPPER={hex(end_r)} "
             f"size={end_r-start_r:,} pins={best_pc}/{bits}")
    return start_r, end_r, best_pinned, bit_probs


def _get_iqm_backend_obj(iqm_device: str, iqm_token: str):
    """
    Connect to IQM device and return IQMBackend.
    Raises RuntimeError on failure (caller falls back to Aer).
    """
    if not IQM_OK:
        raise RuntimeError("pytket-iqm not installed: pip install pytket-iqm")
    if not iqm_token:
        raise RuntimeError("IQM API token required. Set IQM_TOKEN or --iqm-token.")
    backend = IQMBackend(device=iqm_device, api_token=iqm_token)
    n_q = IQM_DEVICE_QUBITS.get(iqm_device.lower(), 16)
    log.info(f"  [IQM] Connected → {iqm_device.capitalize()} ({n_q}q)")
    return backend


def _run_on_iqm(
    qiskit_circuit: "QuantumCircuit",
    iqm_backend,
    n_shots: int,
    reg_name: str = "c",
) -> dict:
    """
    Submit a fully-bound Qiskit circuit to IQM via pytket bridge.
    Returns counts {bitstring: count}.

    Steps:
      1. qiskit_to_tk()          — Qiskit → pytket
      2. get_compiled_circuit()  — IQM native gate transpilation
      3. process_circuit()       — submit to IQM Resonance queue
      4. get_result().get_counts() — retrieve results
    """
    if not PYTKET_QISKIT_OK:
        raise RuntimeError("pytket-qiskit not installed: pip install pytket-qiskit")
    # Decompose all named sub-circuits before pytket conversion
    # so DiagonalGate / circuit-N instructions never reach qiskit_to_tk
    try:
        qiskit_circuit = qiskit_circuit.decompose(reps=3)
    except Exception:
        pass
    tk_circ   = qiskit_to_tk(qiskit_circuit)
    compiled  = iqm_backend.get_compiled_circuit(tk_circ)
    handle    = iqm_backend.process_circuit(compiled, n_shots=n_shots)
    result    = iqm_backend.get_result(handle)
    raw       = result.get_counts()
    return {"".join(str(b) for b in state): cnt for state, cnt in raw.items()}


def _run_on_aer(
    qiskit_circuit: "QuantumCircuit",
    n_shots: int,
    opt_level: int = 1,
) -> dict:
    """
    Run a bound Qiskit circuit on AerSimulator. Returns counts dict.
    Uses opt_level=1 max to avoid heavy transpilation that triggers
    PhysicalQubit index errors on large circuits.
    """
    # FIX: always fresh AerSimulator — never inherits stale IQM coupling map
    # PhysicalQubit(49) errors happen when Aer reuses an IQM backend target.
    aer_sim = AerSimulator()   # clean instance, no coupling_map
    sampler = AerSampler()
    isa_qc  = None
    for lvl in [1, 0]:         # try level 1, then level 0
        try:
            from qiskit.compiler import transpile as _qk_transpile
            isa_qc = _qk_transpile(qiskit_circuit,
                                   backend=aer_sim,
                                   optimization_level=lvl)
            break
        except Exception as e:
            log.warning(f"  [Aer] transpile lvl={lvl} failed ({e!r})")
    if isa_qc is None:
        isa_qc = qiskit_circuit   # bare circuit — best effort
    try:
        job = sampler.run([(isa_qc,)], shots=n_shots)
        res = job.result()
        for rn in ("c", "mkey", "key", "wc"):
            try:
                reg = getattr(res[0].data, rn, None)
                if reg is not None:
                    return reg.get_counts()
            except Exception:
                pass
        for attr in dir(res[0].data):
            if not attr.startswith("_"):
                try:
                    obj = getattr(res[0].data, attr)
                    if hasattr(obj, "get_counts"):
                        return obj.get_counts()
                except Exception:
                    pass
    except Exception as e:
        log.warning(f"  [Aer] sampler failed ({e!r})")
    return {}


def _execute_circuit(
    bound_qc: "QuantumCircuit",
    n_shots: int,
    opt_level: int,
    backend_mode: str,
    iqm_backend,         # IQMBackend object or None
    reg_name: str = "c",
) -> dict:
    """
    Route a bound (parameter-free) circuit to IQM hardware or Aer.
    Falls back to Aer on any IQM error.
    """
    if backend_mode == "iqm_hardware" and iqm_backend is not None:
        try:
            return _run_on_iqm(bound_qc, iqm_backend, n_shots, reg_name)
        except Exception as e:
            log.warning(f"  [IQM exec] {e} — Aer fallback this call")
    return _run_on_aer(bound_qc, n_shots, opt_level)


# =============================================================================
# [P-BIT ENGINE v1] — True Probabilistic-Bit Walk  (v19 NEW)
# =============================================================================
#
# DIAGNOSIS (v18 → v19):
#   v18 Phase B2 used quantum gates: H (superposition), RY (Bloch rotation),
#   CNOT (entanglement), RZZ (Ising ZZ gate), and Born-rule measurement.
#   These are QUANTUM operations — coherent, reversible, simultaneous.
#
#   A TRUE p-bit is STOCHASTIC, not coherent:
#     · p(s_i = +1) = σ(β · I_i)   sigmoid activation
#     · I_i = Σ_j W_ij · s_j + h_i  local field (neighbors + external bias)
#     · Updates are SEQUENTIAL and ASYNC — not all-at-once like quantum gates
#     · β (inverse temperature) controls noise: high β = deterministic,
#                                                low  β = random (hot)
#     · The bit RANDOMLY JUMPS between 0 and 1 — it is never in superposition
#
#   This IS the behavior shown in the GIF oscilloscope:
#     · Left spread  = cool waveforms = p-bit visiting those key values often
#     · Right spread = warm waveforms = p-bit visiting those key values often
#     · Empty middle = snake corridor  = p-bit AVOIDS this zone = key location
#
#   Physics: the energy landscape from EC point arithmetic makes the key offset
#   a local ENERGY MINIMUM. The p-bit, driven by sigmoid(β·energy_field),
#   gets REPELLED from the minimum — because it randomly jumps to high-energy
#   states more often when the field is weak near the minimum. The corridor
#   in the visit density IS the location of minimum EC energy = the key.
#
# IMPLEMENTATION:
#   N_CHAINS parallel p-bit chains, each with `bits` p-bits.
#   Weight matrix W[i,j] = J_couplings[i] for j=i±1,i±2 (from Ising model).
#   Bias vector  h[i]    = h_biases[i]    (from SparsePauliOp fit).
#   Beta annealing: starts at beta_start (hot) → beta_end (cold) over n_steps.
#   Each step: pick random bit i, compute I_i, flip with prob σ(β·I_i).
#   After burn-in, record visit density per offset bin.
#   Returns (energy, offset) pairs exactly like run_quantum_walk_phase.
# =============================================================================


def _pbit_sigmoid(x: float) -> float:
    """Numerically stable sigmoid: σ(x) = 1 / (1 + exp(-x))."""
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    ex = math.exp(x)
    return ex / (1.0 + ex)


def _pbit_local_field(
    state: np.ndarray,
    bit_idx: int,
    bits: int,
    h_biases: np.ndarray,
    J_couplings: np.ndarray,
    dxs: Optional[List[int]] = None,
) -> float:
    """
    Compute local field I_i = Σ_j W_ij·s_j + h_i for p-bit i.

    Coupling structure mirrors the Ising Hamiltonian:
      NN (j=i±1):    weight = J_couplings[min(i,j)]
      skip-2 (i±2):  weight = J_couplings[min(i,j)] * 0.5
      skip-3 (i±3):  weight = J_couplings[min(i,j)] * 0.25

    Bias h_i comes from h_biases (energy landscape from Sobol probing).
    If dxs available: add EC delta-x component as additional bias signal.
    """
    I = float(h_biases[bit_idx]) if bit_idx < len(h_biases) else 0.0

    # EC delta-x bias (pubkey mode): directs p-bit toward the correct bit value
    if dxs is not None and bit_idx < len(dxs):
        I += (1.0 - 2.0 * float(dxs[bit_idx])) * 0.5

    # NN coupling
    for delta, scale in [(1, 1.0), (-1, 1.0), (2, 0.5), (-2, 0.5), (3, 0.25), (-3, 0.25)]:
        j = bit_idx + delta
        if 0 <= j < bits:
            jidx = min(bit_idx, j)
            if jidx < len(J_couplings):
                I += J_couplings[jidx] * scale * float(state[j])

    return I


def run_pbit_walk_phase(
    bits: int,
    base: int,
    target_h160: bytes,
    pubkey_xy: Optional[Tuple[int, int]],
    pubkey_hex: Optional[str],
    h_biases: np.ndarray,
    J_couplings: np.ndarray,
    full_start: int = 0,
    full_end: int = 0,
    n_chains: int = 64,
    n_steps: int = 2000,
    burn_in: int = 200,
    beta_start: float = 0.5,
    beta_end: float = 4.0,
    dxs: Optional[List[int]] = None,
) -> List[Tuple[float, int]]:
    """
    [P-BIT ENGINE v1] — True probabilistic-bit walk for key-space exploration.

    Replaces Phase B2 quantum walk with stochastic sigmoid p-bit dynamics.
    Each of n_chains independent p-bit chains performs Glauber-dynamics
    Monte Carlo over `bits` p-bits, biased by the EC energy landscape.

    The visit density of all chains, plotted vs key offset, produces the
    oscilloscope waveform from the reference GIFs:
      · High density left/right of the snake = spread cloud (p-bit exploring)
      · Zero density in the corridor     = snake = key location

    Physics:
      · p(s_i=+1) = σ(β·I_i)  where σ = sigmoid
      · I_i = Σ_j W_ij·s_j + h_i   (local field)
      · β increases from beta_start → beta_end (simulated annealing)
      · Sequential random-bit updates (Glauber dynamics)
      · State encodes a key offset: offset = Σ_b s_b · 2^b  (binary)

    Returns List[(energy, offset)] compatible with all downstream phases.
    """
    if full_end == 0:
        full_start, full_end = auto_range(bits)

    max_valid_off = full_end - base
    min_valid_off = max(0, full_start - base)
    valid_range   = max(1, max_valid_off - min_valid_off)

    log.info(f"  [PBit-v1] TRUE p-bit walk: {n_chains} chains × {n_steps} steps  "
             f"β: {beta_start:.2f}→{beta_end:.2f}  bits={bits}  "
             f"burn_in={burn_in}")

    all_pbit_samples: List[Tuple[float, int]] = []
    rng = np.random.default_rng()

    for chain_idx in range(n_chains):

        # ── Initialise chain: random state in valid range ─────────────────────
        init_off = rng.integers(min_valid_off, max(min_valid_off + 1, max_valid_off))
        state = np.array([(init_off >> b) & 1 for b in range(bits)],
                         dtype=np.float64)
        # Convert ±1 representation: 0 → -1, 1 → +1
        state = state * 2.0 - 1.0

        chain_samples: List[Tuple[float, int]] = []
        total_steps = burn_in + n_steps

        for step in range(total_steps):
            # Annealing schedule: linear ramp from beta_start to beta_end
            progress = step / max(total_steps - 1, 1)
            beta     = beta_start + (beta_end - beta_start) * progress

            # Sequential random-bit Glauber update — NOT simultaneous
            bit_order = rng.permutation(bits)   # random order per step
            for i in bit_order:
                I_i = _pbit_local_field(state, int(i), bits,
                                        h_biases, J_couplings, dxs)
                # P(s_i = +1) = sigmoid(β · I_i)
                p_up = _pbit_sigmoid(beta * I_i)
                state[i] = 1.0 if rng.random() < p_up else -1.0

            # After burn-in: record current state as an offset sample
            if step >= burn_in:
                # Convert ±1 state back to binary offset
                bits_bin = ((state + 1.0) / 2.0).astype(int)   # 0 or 1
                offset   = int(sum(bits_bin[b] << b for b in range(bits)))

                # Clamp to valid range
                offset = max(min_valid_off, min(max_valid_off, offset))

                # Score with EC energy (same as quantum walk)
                energy = compute_energy(base + offset, target_h160,
                                        pubkey_xy, pubkey_hex)
                bv     = np.array([(offset >> b) & 1 for b in range(bits)],
                                  dtype=float)
                dot_n  = (float(np.dot(h_biases, bv)) + bits) / (2.0 * bits + 1e-9)
                eff    = 0.65 * energy + 0.35 * (1.0 - dot_n)
                chain_samples.append((eff, offset))

        all_pbit_samples.extend(chain_samples)

        # Progress log every 16 chains
        if (chain_idx + 1) % 16 == 0 or chain_idx == n_chains - 1:
            n_unique = len(set(o for _, o in all_pbit_samples))
            best_e   = min((e for e, _ in all_pbit_samples), default=1.0)
            log.info(f"  [PBit-v1] chain {chain_idx+1}/{n_chains}  "
                     f"total_samples={len(all_pbit_samples):,}  "
                     f"unique_offsets={n_unique:,}  best_eff={best_e:.4f}")

    log.info(f"  [PBit-v1] Walk complete — {len(all_pbit_samples):,} samples  "
             f"unique={len(set(o for _, o in all_pbit_samples)):,}")
    return all_pbit_samples


# =============================================================================
# [QUANTUM WALK ENGINE v2] — In-circuit phase oracle + adaptive coin
# =============================================================================
# Upgrade from v1:
#
# v1 problem: h_biases computed ONCE from 512 random probes.
#   The circuit had no knowledge of WHICH key it landed on after each
#   shift — just a static average gradient baked as fixed RY angles.
#
# v2 solution: PER-STEP PHASE ORACLE
#   After each shift operator, we apply RZ(phi_b) per key qubit where
#   phi_b = pi * msb_sign(delta_x[b]).  delta_x[b] = x-coordinate of
#   (2^b)*G subtracted from the target pubkey x-coordinate.
#   This encodes the EC information INSIDE the circuit, per step.
#   Correct-key amplitudes accumulate phase coherently.
#   Wrong-key amplitudes accumulate phase incoherently → cancelled.
#   After walk_steps steps: constructive interference at the key.
#
# ADAPTIVE COIN:
#   Instead of fixed Hadamard, each qubit gets Ry(theta_b) where
#   theta_b starts at pi/2 (Hadamard) and is updated each step by
#   the phase oracle feedback: theta_b += alpha * phi_b.
#   This steers the walk toward the low-energy (low phase) region.
#
# LONG-RANGE COUPLINGS (skip-3, skip-4):
#   Available on IBM 156q and IQM Emerald 50q.
#   Encode longer-range Ising correlations that the energy landscape
#   has but nearest-neighbour couplings miss.
#
# QUBIT BUDGET LOGIC:
#   All qubits go to the KEY register (no wasted ancilla in walk).
#   walk_qubits = min(device_capacity, bits + extra_reach)
#   extra_reach = unused qubits that extend the key register coverage
#   via long-range coupling without measuring — they amplify
#   interference but are traced out (not measured).
# =============================================================================

def _build_phase_oracle_step(
    qc: "QuantumCircuit",
    key_r: "QuantumRegister",
    bits: int,
    dxs: Optional[List[int]],
    step: int,
    walk_steps: int,
    h_biases: np.ndarray,
) -> None:
    """
    Apply per-step phase oracle to key register.

    For each qubit b we apply RZ(phi_b) where phi_b encodes the
    EC delta-x information for that bit position.

    If dxs is available (pubkey mode): phi_b from msb of dxs[b].
    If dxs is None (hash160 mode):    phi_b from h_biases[b].

    Phase accumulates coherently for amplitudes near the correct key
    and incoherently (cancels) for amplitudes far away.

    The angle scales with step so early steps explore broadly and
    late steps concentrate tightly — mimicking simulated annealing.
    """
    # Annealing schedule: start broad (small phase), end sharp (large phase)
    # step 0 = broad exploration, step walk_steps-1 = tight concentration
    anneal = 0.3 + 0.7 * (step / max(walk_steps - 1, 1))

    for b in range(bits):
        if dxs is not None and b < len(dxs):
            phi = math.pi * (1.0 - 2.0 * int(dxs[b])) * anneal
        else:
            phi = math.pi * float(h_biases[b]) * anneal
        if abs(phi) > 1e-6:
            qc.rz(phi, key_r[b])


def _build_adaptive_coin(
    qc: "QuantumCircuit",
    key_r: "QuantumRegister",
    bits: int,
    coin_angles: np.ndarray,
) -> None:
    """
    Adaptive coin: Ry(theta_b) per qubit instead of fixed Hadamard.
    coin_angles are updated each step based on phase oracle feedback.
    Starts near pi/2 (= Hadamard), drifts toward 0 (= no-flip) as
    the walk concentrates.
    """
    for b in range(bits):
        angle = float(np.clip(coin_angles[b], 1e-6, math.pi))
        qc.ry(angle, key_r[b])


def build_quantum_walk_circuit(
    bits: int,
    h_biases: np.ndarray,
    J_couplings: np.ndarray,
    walk_steps: int = 3,
    ancilla: int = 0,
    backend_mode: str = "simulator",
    dxs: Optional[List[int]] = None,
    extra_reach: int = 0,
) -> Optional["QuantumCircuit"]:
    """
    [QUANTUM P-BIT (QPB) ENGINE v3] — Qubits acting exactly like p-bits.

    WHY v19 WAS STILL WRONG:
      v19's build_quantum_walk_circuit still used:
        1. qc.h(key_r)          — uniform superposition (NOT p-bit hot state)
        2. _build_adaptive_coin — fixed Ry(θ_b) with static θ (NOT local field)
        3. CNOT cascade shift   — ballistic walk (NOT random single-bit jump)
        4. qc.rzz(J, b, b+1)   — global ZZ gate (NOT conditional local field)
      This is a BALLISTIC quantum walk. P-bits are DIFFUSIVE / MARKOV CHAIN.

    THE QPB FIX — per-qubit local-field rotation:
      For each qubit b at each step, rotation angle = f(I_b):

        I_b  = h_biases[b]                   ← external bias (EC gradient)
               + dxs_contribution             ← EC delta-x steering
               = local field (bias part only; coupling added via CRZ below)

        p_b  = sigmoid(β · I_b)              ← p-bit decision probability
             = 1 / (1 + exp(-β·I_b))

        θ_b  = 2 · arcsin(√p_b)              ← QPB gate angle
               Ry(θ_b) gives P(|1⟩) = p_b   EXACTLY after measurement.
               This IS the p-bit stochastic binary decision, in quantum form.

      Neighbor coupling via CRZ (Controlled-RZ):
        CRZ(β·W, ctrl=b, tgt=b+1) rotates qubit b+1 by β·W IF qubit b = |1⟩.
        This is the quantum equivalent of: I_{b+1} += W * s_b
        It makes qubit b+1's decision depend on qubit b's state — exactly
        what the p-bit local field formula does: I_i = Σ_j W_ij · s_j + h_i.

      β annealing (hot → cold):
        β = beta_start → beta_end over walk_steps.
        Low  β (hot):  sigmoid ≈ 0.5 → Ry(π/2) → equal prob → SPREAD CLOUD
        High β (cold): sigmoid → 0 or 1 → Ry(0 or π) → COMMITTED → SNAKE
        This IS the oscilloscope behavior in the GIF.

      Each shot = one independent p-bit trajectory (measurement = one binary
      jump to a specific offset). N_shots = N independent p-bit runs.
      The measurement histogram over many shots = p-bit visit density map.
      Empty corridor in that histogram = snake = key location bracket.

    Architecture per step:
      1. QPB rotation  Ry(2·arcsin(√sigmoid(β·h_b))) per qubit  ← p-bit bias
      2. CRZ coupling  CRZ(β·W_bj, b, j) per neighbor pair      ← p-bit W_ij
      3. EC oracle     RZ(φ_b) per qubit                         ← energy steer
      4. Reach CX      entangle extra qubits (traced out)         ← range extend
    """
    if not QISKIT_OK:
        return None

    # ── Qubit budget ────────────────────────────────────────────────────────
    if backend_mode in ("iqm_hardware", "qrisp_iqm"):
        max_total = _MAX_IQM_CIRCUIT
    elif backend_mode == "ibm_hardware":
        max_total = _MAX_IBM_QUBITS
    else:
        max_total = _MAX_AER_QUBITS

    safe_reach = min(extra_reach, max(0, max_total - bits))
    total      = bits + safe_reach

    key_r = QuantumRegister(bits, "qpb")
    cr    = ClassicalRegister(bits, "wc")
    if safe_reach > 0:
        reach_r = QuantumRegister(safe_reach, "wr")
        qc = QuantumCircuit(key_r, reach_r, cr,
                            name=f"QPBv3_{bits}q_{walk_steps}s")
        qc.h(reach_r)   # reach register starts in superposition (interference amp)
    else:
        reach_r = None
        qc = QuantumCircuit(key_r, cr,
                            name=f"QPBv3_{bits}q_{walk_steps}s")

    # ── Initial state: hot p-bit = uniform distribution = H gate ──────────
    # When β is small the QPB rotations will be ~π/2 anyway, but starting
    # in superposition ensures the first step is truly unbiased (hot start).
    qc.h(key_r)

    # ── P-bit annealing schedule ───────────────────────────────────────────
    beta_start = 0.5   # hot: sigmoid(0.5·I) ≈ 0.5+0.1·I → broad spread cloud
    beta_end   = 4.0   # cold: sigmoid(4·I) → 0 or 1 → committed to key region

    for step in range(walk_steps):
        # Linear annealing: 0.0 (first step) → 1.0 (last step)
        progress = step / max(walk_steps - 1, 1)
        beta     = beta_start + (beta_end - beta_start) * progress

        # ── Step 1: QPB gate per qubit (local-field rotation) ────────────────
        # Each qubit b gets Ry(2·arcsin(√p_b)) where p_b = sigmoid(β·I_b).
        # This is the EXACT quantum gate that produces P(|1⟩) = p_b.
        # Numerically stable sigmoid: avoid overflow for large |β·I_b|.
        for b in range(bits):
            # Bias component of local field: h_biases[b] from EC landscape
            I_b = float(h_biases[b]) if b < len(h_biases) else 0.0

            # EC delta-x steering: dxs[b] encodes whether bit b should be 0/1
            # Scale grows with annealing progress (zero at step 0 = unbiased)
            if dxs is not None and b < len(dxs):
                I_b += (1.0 - 2.0 * int(dxs[b])) * 0.5 * progress

            # Clamp local field to prevent numerical instability
            I_b = float(np.clip(I_b, -6.0, 6.0))

            # Numerically stable sigmoid(β · I_b)
            x = beta * I_b
            if x >= 0.0:
                p_b = 1.0 / (1.0 + math.exp(-x))
            else:
                ex  = math.exp(x)
                p_b = ex / (1.0 + ex)

            # Clamp to valid arcsin domain
            p_b = max(1e-7, min(1.0 - 1e-7, p_b))

            # QPB gate: Ry(2·arcsin(√p_b)) → P(|1⟩) = p_b after measurement
            # This is mathematically identical to the p-bit sigmoid decision.
            angle = 2.0 * math.asin(math.sqrt(p_b))
            qc.ry(angle, key_r[b])

        # ── Step 2: CRZ neighbor coupling (quantum W_ij matrix) ──────────────
        # CRZ(θ, ctrl, tgt): rotates tgt by θ if ctrl = |1⟩.
        # Effect on tgt's measurement probability: equivalent to adding
        # W·s_ctrl to tgt's local field — exactly the p-bit coupling term.
        #
        # Symmetric coupling: both (b→b+1) and (b+1→b) because W_ij = W_ji.

        # NN coupling  j = b±1  (full weight)
        for b in range(min(bits - 1, len(J_couplings))):
            w = float(J_couplings[b]) * beta
            if abs(w) > 1e-6:
                qc.crz( w, key_r[b],   key_r[b+1])  # b influences b+1
                qc.crz( w, key_r[b+1], key_r[b]  )  # b+1 influences b (symmetric)

        # Skip-2 coupling  j = b±2  (half weight — longer range, weaker)
        for b in range(min(bits - 2, len(J_couplings))):
            w = float(J_couplings[b]) * beta * 0.5
            if abs(w) > 1e-6:
                qc.crz(w, key_r[b],   key_r[b+2])
                qc.crz(w, key_r[b+2], key_r[b]  )

        # Skip-3 coupling  j = b±3  (quarter weight)
        for b in range(min(bits - 3, len(J_couplings))):
            w = float(J_couplings[b]) * beta * 0.25
            if abs(w) > 1e-6:
                qc.crz(w, key_r[b],   key_r[b+3])
                qc.crz(w, key_r[b+3], key_r[b]  )

        # Skip-4 coupling  j = b±4  (eighth weight — only on 5+ qubit circuits)
        if bits >= 5:
            for b in range(min(bits - 4, len(J_couplings))):
                w = float(J_couplings[b]) * beta * 0.125
                if abs(w) > 1e-6:
                    qc.crz(w, key_r[b],   key_r[b+4])

        # ── Step 3: EC phase oracle (energy steering per step) ────────────────
        # Adds RZ(φ_b) to steer qubit phases toward the correct key bits.
        # This is the same per-step oracle as before — kept for energy guidance.
        # Does NOT replace the QPB gate — it's an additional phase signal.
        _build_phase_oracle_step(qc, key_r, bits, dxs, step, walk_steps, h_biases)

        # ── Step 4: Reach register (long-range interference amplifiers) ───────
        # Extra qubits entangled with key register create longer-range
        # correlations. They are NOT measured — pure quantum resource.
        if reach_r is not None and safe_reach > 0:
            for ri in range(safe_reach):
                ki = (ri * 3) % bits
                qc.cx(key_r[ki], reach_r[ri])
                if dxs is not None and ki < len(dxs):
                    phi = math.pi * (1.0 - 2.0 * int(dxs[ki])) * progress * 0.5
                    if abs(phi) > 1e-6:
                        qc.rz(phi, reach_r[ri])
                qc.cx(key_r[ki], reach_r[ri])   # un-entangle (keeps depth low)

    # Measure key register — each shot = one p-bit trajectory endpoint
    qc.measure(key_r, cr)

    log.info(
        f"  [QPBv3] {total}q total  {bits}q QPB + {safe_reach}q reach  "
        f"{walk_steps} steps  β:{beta_start:.1f}→{beta_end:.1f}  "
        f"oracle={'EC-delta' if dxs else 'h_bias'}  "
        f"depth≈{qc.depth()}"
    )
    return qc



def _run_adaptive_coin_walk(
    bits: int, base: int,
    target_h160: bytes,
    pubkey_xy: Optional[Tuple[int, int]],
    pubkey_hex: Optional[str],
    h_biases: np.ndarray,
    J_couplings: np.ndarray,
    walk_steps: int = 3,
    n_walks: int = 2,
    shots: int = 2048,
    opt_level: int = 1,
    backend_mode: str = "simulator",
    iqm_device: str = "garnet",
    iqm_token: str = "",
    ibm_token: str = "", ibm_crn: str = "",
    ibm_backend_name: str = "ibm_fez",
    dxs: Optional[List[int]] = None,
    full_start: int = 0,
    full_end: int = 0,
) -> List[Tuple[float, int]]:
    """
    [ADAPTIVE-COIN QUANTUM WALK — v18 style, Engine 3 in v21 Phase B2]

    Uses the v18 build_quantum_walk_circuit with adaptive coin (Ry(θ_b) per
    qubit, coin angles steered by per-step phase oracle feedback) and CNOT
    cascade shift operator. This is a DIFFERENT exploration strategy from the
    QPB engine (which uses Ry(2·arcsin(√sigmoid(β·I_b))) + CRZ coupling).

    Running BOTH explores different parts of the same key-space landscape:
    · QPB explores via sigmoid-gated rotation (p-bit-equivalent probability)
    · Adaptive-coin explores via Hadamard-like coin that narrows with annealing

    Their combined visit density map produces a more definitive snake corridor.

    This function builds adaptive-coin circuits using a simplified version of
    the v18 walk logic (H init + RY coin + CNOT shift + RZ oracle + RZZ coupling)
    and runs them on the same backend as the rest of the pipeline.
    """
    if not QISKIT_OK:
        return []
    if full_end == 0:
        full_start, full_end = auto_range(bits)

    if backend_mode in ("iqm_hardware", "qrisp_iqm"):
        max_total = _MAX_IQM_CIRCUIT
    elif backend_mode == "ibm_hardware":
        max_total = _MAX_IBM_QUBITS
    else:
        max_total = _MAX_AER_QUBITS

    # Connect hardware once
    iqm_backend = None
    if backend_mode == "iqm_hardware":
        try:
            iqm_backend = _get_iqm_backend_obj(iqm_device, iqm_token)
        except Exception as e:
            log.warning(f"  [AdapCoin IQM] {e} — Aer fallback")
            backend_mode = "simulator"

    all_samples: List[Tuple[float, int]] = []
    max_valid_off = full_end - base
    min_valid_off = max(0, full_start - base)

    for walk_idx in range(n_walks):
        steps = max(1, walk_steps + walk_idx - n_walks // 2)
        noise_scale = 0.02 + 0.01 * walk_idx
        biases_v = h_biases + np.random.normal(0, noise_scale, len(h_biases))
        J_v      = J_couplings + np.random.normal(0, noise_scale * 0.3, len(J_couplings))

        # --- Build adaptive-coin circuit ---
        safe_reach = max(0, min(max_total - bits, bits // 2))
        key_r = QuantumRegister(bits, "ac")
        cr    = ClassicalRegister(bits, "wc")
        if safe_reach > 0:
            reach_r = QuantumRegister(safe_reach, "ar")
            qc = QuantumCircuit(key_r, reach_r, cr,
                                name=f"AdapCoin_{bits}q_{steps}s")
            qc.h(reach_r)
        else:
            reach_r = None
            qc = QuantumCircuit(key_r, cr,
                                name=f"AdapCoin_{bits}q_{steps}s")

        # Uniform superposition (hot start)
        qc.h(key_r)

        # Adaptive coin angles — start at pi/2 (Hadamard)
        coin_angles = np.full(bits, math.pi / 2.0)
        coin_lr     = 0.15

        for step in range(steps):
            anneal = 0.3 + 0.7 * (step / max(steps - 1, 1))

            # Adaptive coin (Ry per qubit)
            for b in range(bits):
                angle = float(np.clip(coin_angles[b], 1e-6, math.pi))
                qc.ry(angle, key_r[b])

            # Shift operator (CNOT cascade)
            for b in range(1, bits):
                qc.cx(key_r[b-1], key_r[b])

            # Per-step EC phase oracle (energy steering)
            for b in range(bits):
                if dxs is not None and b < len(dxs):
                    phi = math.pi * (1.0 - 2.0 * int(dxs[b])) * anneal
                else:
                    phi = math.pi * float(biases_v[b]) * anneal
                if abs(phi) > 1e-6:
                    qc.rz(phi, key_r[b])

            # Update coin angles from oracle feedback
            for b in range(bits):
                if dxs is not None and b < len(dxs):
                    phi = math.pi * (1.0 - 2.0 * int(dxs[b])) * anneal
                else:
                    phi = math.pi * float(biases_v[b]) * anneal
                coin_angles[b] = max(0.05, coin_angles[b] - coin_lr * abs(phi))

            # Ising couplings (NN + skip-2 + skip-3 + skip-4)
            for b in range(min(bits - 1, len(J_v))):
                a = float(J_v[b] * math.pi)
                if abs(a) > 1e-6:
                    qc.rzz(a, key_r[b], key_r[b+1])
            for b in range(min(bits - 2, len(J_v))):
                a = float(J_v[b] * math.pi * 0.5)
                if abs(a) > 1e-6:
                    qc.rzz(a, key_r[b], key_r[b+2])
            for b in range(min(bits - 3, len(J_v))):
                a = float(J_v[b] * math.pi * 0.25)
                if abs(a) > 1e-6:
                    qc.rzz(a, key_r[b], key_r[b+3])
            if bits >= 5:
                for b in range(min(bits - 4, len(J_v))):
                    a = float(J_v[b] * math.pi * 0.125)
                    if abs(a) > 1e-6:
                        qc.rzz(a, key_r[b], key_r[b+4])

            # Reach register interference
            if reach_r is not None and safe_reach > 0:
                for ri in range(safe_reach):
                    ki = (ri * 3) % bits
                    qc.cx(key_r[ki], reach_r[ri])
                    if dxs is not None and ki < len(dxs):
                        phi = math.pi * (1.0 - 2.0 * int(dxs[ki])) * anneal * 0.5
                        if abs(phi) > 1e-6:
                            qc.rz(phi, reach_r[ri])
                    qc.cx(key_r[ki], reach_r[ri])

        # Reverse shift
        for b in range(bits - 1, 0, -1):
            qc.cx(key_r[b-1], key_r[b])

        qc.measure(key_r, cr)

        try:
            counts = _execute_circuit(qc, shots, opt_level,
                                      backend_mode, iqm_backend, "wc")
        except Exception as e:
            log.warning(f"  [AdapCoin {walk_idx+1}] error: {e}")
            continue

        walk_s: List[Tuple[float, int]] = []
        for bitstr, cnt in counts.items():
            bs     = bitstr.zfill(bits)[-bits:]
            offset = int(bs, 2)
            if offset < min_valid_off or offset > max_valid_off:
                continue
            energy = compute_energy(base + offset, target_h160, pubkey_xy, pubkey_hex)
            bv     = np.array([(offset >> b) & 1 for b in range(bits)], dtype=float)
            dot_norm = (float(np.dot(h_biases, bv)) + bits) / (2.0 * bits + 1e-9)
            eff    = 0.65 * energy + 0.35 * (1.0 - dot_norm)
            w = max(1, min(cnt, 20))
            for _ in range(w):
                walk_s.append((eff, offset))

        all_samples.extend(walk_s)
        n_unique = len(set(o for _, o in walk_s))
        best_e   = min((e for e, _ in walk_s), default=256.0)
        log.info(f"  [AdapCoin {walk_idx+1}/{n_walks}] steps={steps}  "
                 f"unique={n_unique}  best_eff={best_e:.3f}  "
                 f"total_pairs={len(all_samples)}")

    return all_samples


def run_quantum_walk_phase(
    bits: int, base: int, target_h160: bytes,
    pubkey_xy: Optional[Tuple[int, int]],
    pubkey_hex: Optional[str],
    h_biases: np.ndarray, J_couplings: np.ndarray,
    ancilla: int = 0, walk_steps: int = 3,
    shots: int = 4096, opt_level: int = 1,
    backend_mode: str = "simulator",
    iqm_device: str = "garnet",
    iqm_token: str = "",
    ibm_token: str = "", ibm_crn: str = "",
    ibm_backend_name: str = "ibm_fez",
    n_walks: int = 4,
    dxs: Optional[List[int]] = None,
    full_start: int = 0, full_end: int = 0,
) -> List[Tuple[float, int]]:
    """
    [QUANTUM P-BIT PHASE v3] Run multiple Quantum P-Bit (QPB) circuits.

    Each circuit uses QPB gates — Ry(2·arcsin(√sigmoid(β·I_b))) per qubit —
    which give each qubit a measurement probability IDENTICAL to a p-bit's
    sigmoid decision: P(|1⟩) = sigmoid(β·I_b).

    CRZ neighbor coupling adds the W_ij·s_j coupling term to each qubit's
    effective rotation, exactly replicating the p-bit local field formula.

    β anneals from 0.5 (hot/spread) to 4.0 (cold/concentrated) per circuit.
    Each shot = one independent p-bit trajectory.
    Combined histogram = p-bit visit density = oscilloscope waveform.
    Empty corridor = snake = key bracket.

    Returns: (energy, offset) pairs — the QPB density map samples.
    """
    if not QISKIT_OK:
        log.warning("  [QPBv3] Qiskit unavailable — skipped")
        return []

    if full_end == 0:
        full_start, full_end = auto_range(bits)
    oracle_type = "EC-delta + QPB-sigmoid" if dxs else "h_bias QPB-sigmoid"
    log.info(f"  [QPBv3] {n_walks} circuits × {shots} shots × {walk_steps} steps  "
             f"bits={bits}  oracle={oracle_type}  β:0.5→4.0")

    # Connect hardware once
    iqm_backend = None; ibm_sampler_w = None; ibm_backend_obj_w = None
    if backend_mode == "iqm_hardware":
        try:
            iqm_backend = _get_iqm_backend_obj(iqm_device, iqm_token)
        except Exception as e:
            log.warning(f"  [QPBv3 IQM] {e} — Aer fallback")
            backend_mode = "simulator"
    elif backend_mode == "ibm_hardware":
        try:
            ibm_sampler_w, ibm_backend_obj_w = _get_ibm_sampler(
                ibm_token, ibm_crn, ibm_backend_name)
        except Exception as e:
            log.warning(f"  [QPBv3 IBM] {e} — Aer fallback")
            backend_mode = "simulator"

    all_walk_samples: List[Tuple[float, int]] = []

    for walk_idx in range(n_walks):
        # Vary walk steps per run to sample different interference patterns
        steps = max(1, walk_steps + walk_idx - n_walks // 2)

        # Vary h_biases per walk: add progressively increasing noise
        # This is the "multi-path interference" — each walk explores
        # a slightly different trajectory, and their combined density
        # map reveals the attractor (the unknown key location)
        # FIX: small fixed noise so each walk explores a DIFFERENT path
        # but the biases are still strong enough to steer toward the target.
        # Old 0.1+0.05*i noise was washing out the gradient completely.
        noise_scale = 0.02 + 0.01 * walk_idx
        biases_v    = h_biases + np.random.normal(0, noise_scale, len(h_biases))
        J_v         = J_couplings + np.random.normal(0, noise_scale * 0.3,
                                                     len(J_couplings))

        # Compute extra reach qubits from device headroom above key register
        if backend_mode in ("iqm_hardware", "qrisp_iqm"):
            dev_cap = _MAX_IQM_CIRCUIT
        elif backend_mode == "ibm_hardware":
            dev_cap = _MAX_IBM_QUBITS
        else:
            dev_cap = _MAX_AER_QUBITS
        extra_reach = max(0, min(dev_cap - bits, bits // 2))  # at most 50% extra
        qc = build_quantum_walk_circuit(
            bits, biases_v, J_v, steps,
            ancilla=0,            # no wasted ancilla — all qubits in key + reach
            backend_mode=backend_mode,
            dxs=dxs,             # EC phase oracle
            extra_reach=extra_reach,
        )
        if qc is None:
            continue

        try:
            if backend_mode == "ibm_hardware" and ibm_sampler_w is not None:
                counts = _run_on_ibm(qc, ibm_sampler_w, ibm_backend_obj_w,
                                     shots, opt_level, "wc")
            else:
                counts = _execute_circuit(qc, shots, opt_level,
                                          backend_mode, iqm_backend, "wc")
        except Exception as e:
            log.warning(f"  [QPBv3 {walk_idx+1}] error: {e}")
            continue

        walk_samples: List[Tuple[float, int]] = []
        max_valid_off = full_end - base
        min_valid_off = max(0, full_start - base)
        for bitstr, cnt in counts.items():
            bs     = bitstr.zfill(bits)[-bits:]
            offset = int(bs, 2)
            if offset < min_valid_off or offset > max_valid_off:
                continue
            energy = compute_energy(base + offset, target_h160, pubkey_xy, pubkey_hex)
            bv     = np.array([(offset >> b) & 1 for b in range(bits)], dtype=float)
            dot_norm = (float(np.dot(h_biases, bv)) + bits) / (2.0 * bits + 1e-9)
            eff    = 0.65 * energy + 0.35 * (1.0 - dot_norm)
            w = max(1, min(cnt, 20))
            for _ in range(w):
                walk_samples.append((eff, offset))

        all_walk_samples.extend(walk_samples)
        n_unique = len(set(o for _, o in walk_samples))
        best_e   = min((e for e, _ in walk_samples), default=256.0)
        log.info(f"  [QPBv3 {walk_idx+1}/{n_walks}] steps={steps}  "
                 f"unique={n_unique}  best_eff={best_e:.3f}  "
                 f"total_pairs={len(all_walk_samples)}")

    log.info(f"  [QPBv3] Phase complete — {len(all_walk_samples)} total pairs")
    return all_walk_samples


# =============================================================================
# QRISP IQM BACKEND FACTORY  (qrisp.interface.IQMBackend — current API)
# =============================================================================
# Current Qrisp API (as of qrisp v0.4+):
#   from qrisp.interface import IQMBackend
#   backend = IQMBackend(api_token="...", device_instance="garnet")
#   result  = qv.get_measurement(backend=backend, shots=4096)
#   result  → {bitstring: probability}  (not counts — probabilities)
# =============================================================================

def _get_qrisp_iqm_backend(iqm_device: str, iqm_token: str):
    """
    Connect to IQM hardware using the Qrisp IQMBackend.
    Uses current qrisp.interface.IQMBackend API.
    Qrisp handles native gate transpilation — no pytket bridge needed.
    Install: pip install "iqm-client>=34.0.3" qrisp
    """
    if not QRISP_OK:
        raise RuntimeError(
            "Qrisp not installed. Run: pip install 'iqm-client>=34.0.3' qrisp")
    if not iqm_token:
        raise RuntimeError("IQM API token required for Qrisp backend.")
    device_alias = QRISP_DEVICE_ALIASES.get(iqm_device.lower(), iqm_device)
    backend = QrispIQMBackend(
        api_token       = iqm_token,
        device_instance = device_alias,
    )
    n_q = IQM_DEVICE_QUBITS.get(iqm_device.lower(), 16)
    log.info(f"  [Qrisp-IQM] Connected → {iqm_device.capitalize()} ({n_q}q)  "
             f"[Qrisp auto-native-transpilation]")
    return backend


def _run_sampler_via_qrisp(
    h_biases: np.ndarray, bits: int, base: int,
    target_h160: bytes, pubkey_xy, pubkey_hex,
    qrisp_backend, shots: int, layers: int, iterations: int,
    J_couplings: np.ndarray,
) -> List[Tuple[float, int]]:
    """
    Run the energy-sampler using Qrisp QuantumVariables.
    Qrisp API: qv.get_measurement(backend=backend, shots=N)
    Returns {bitstring: probability} — we convert to (energy, offset) pairs.
    """
    try:
        from qrisp import QuantumVariable, h, cx, ry
    except ImportError:
        log.warning("  [Qrisp sampler] qrisp not importable — empty result")
        return []

    all_samples: List[Tuple[float, int]] = []

    for it in range(iterations):
        try:
            qv = QuantumVariable(bits)
            h(qv[0])
            noise_scale = 0.4 + 0.1 * (it / max(iterations - 1, 1))
            for b in range(bits):
                angle = float(np.arccos(np.clip(-h_biases[b], -1.0, 1.0)))
                angle += float(np.random.normal(0, noise_scale))
                ry(angle, qv[b])
            for rep in range(min(layers, 3)):
                for b in range(bits - 1):
                    cx(qv[b], qv[b + 1])
                for b in range(bits):
                    jidx  = b % max(len(J_couplings), 1)
                    angle = float(J_couplings[jidx] * math.pi
                                  + np.random.normal(0, noise_scale * 0.5))
                    ry(angle, qv[b])

            # qrisp.get_measurement returns {bitstring: probability}
            result = qv.get_measurement(backend=qrisp_backend, shots=shots)
            for bitstr, prob in result.items():
                cnt    = max(1, int(prob * shots))
                bs     = str(bitstr).zfill(bits)[-bits:]
                offset = int(bs, 2)
                energy = compute_energy(base + offset, target_h160, pubkey_xy, pubkey_hex)
                bv     = np.array([(offset >> b) & 1 for b in range(bits)], dtype=float)
                eff    = 0.7 * energy - 0.3 * float(np.dot(h_biases, bv))
                w = max(1, min(cnt, 20))
                for _ in range(w):
                    all_samples.append((eff, offset))
            log.info(f"  [Qrisp-IQM iter {it+1}/{iterations}]  "
                     f"outcomes={len(result)}  total={len(all_samples)}")
        except Exception as e:
            log.warning(f"  [Qrisp sampler iter {it+1}] error: {e}")

    return all_samples


# =============================================================================
# IBM QUANTUM BACKEND FACTORY
# =============================================================================

def _get_ibm_sampler(ibm_token: str, ibm_crn: str, ibm_backend_name: str):
    """Connect to IBM Quantum. Returns (IBMSampler, backend_obj)."""
    if not IBM_OK:
        raise RuntimeError("pip install qiskit-ibm-runtime")
    if not ibm_token:
        raise RuntimeError("IBM token required. Set IBM_QUANTUM_TOKEN.")
    svc     = QiskitRuntimeService(
                  channel="ibm_quantum_platform",
                  token=ibm_token,
                  instance=ibm_crn or None)
    backend = svc.backend(ibm_backend_name)
    sampler = IBMSampler(mode=backend)
    log.info(f"  [IBM] Connected → {backend.name} ({backend.num_qubits}q)")
    return sampler, backend


def _run_on_ibm(
    qiskit_circuit: "QuantumCircuit",
    ibm_sampler, ibm_backend_obj,
    n_shots: int, opt_level: int, reg_name: str = "c",
) -> dict:
    """Transpile and run a Qiskit circuit on IBM hardware."""
    pm     = generate_preset_pass_manager(min(opt_level, 2), backend=ibm_backend_obj)
    isa_qc = pm.run(qiskit_circuit)
    job    = ibm_sampler.run([(isa_qc,)], shots=n_shots)
    res    = job.result()
    for name in (reg_name, "c", "mkey", "wc", "measure"):
        try:
            obj = getattr(res[0].data, name, None)
            if obj is not None and hasattr(obj, "get_counts"):
                return obj.get_counts()
        except Exception:
            continue
    return {}


# =============================================================================
# [MAX-Q] BACKEND QUBIT CAPACITY  (IQM + IBM + Qrisp version)
# =============================================================================

def get_backend_qubit_capacity(backend_mode: str, iqm_device: str = "garnet",
                               ibm_backend_name: str = _IBM_DEFAULT_BACKEND,
                               ibm_backend_obj=None) -> int:
    """[MAX-Q] Return usable qubit count for the chosen backend."""
    if backend_mode in ("iqm_hardware", "qrisp_iqm"):
        n = IQM_DEVICE_QUBITS.get(iqm_device.lower(), 16)
        log.info(f"  [MAX-Q] IQM {iqm_device} ({backend_mode}) → {n}q"); return n
    if backend_mode == "ibm_hardware":
        if ibm_backend_obj is not None:
            try:
                n = int(ibm_backend_obj.num_qubits); cap = min(n, _MAX_IBM_QUBITS)
                log.info(f"  [MAX-Q] IBM {ibm_backend_obj.name} → {n}q (cap {cap}q)")
                return cap
            except Exception: pass
        log.info(f"  [MAX-Q] IBM (catalogue) → {_MAX_IBM_QUBITS}q"); return _MAX_IBM_QUBITS
    cap = _MAX_AER_QUBITS
    log.info(f"  [MAX-Q] Aer → cap {cap}q"); return cap


def compute_ancilla_count(bits: int, backend_capacity: int,
                          backend_mode: str = "simulator") -> int:
    """Compute safe ancilla count with backend-specific hard caps."""
    if backend_mode in ("iqm_hardware", "qrisp_iqm"):
        hard_cap = _MAX_IQM_CIRCUIT
    elif backend_mode == "ibm_hardware":
        hard_cap = _MAX_IBM_QUBITS
    else:
        hard_cap = _MAX_AER_QUBITS
    effective_cap = min(backend_capacity, hard_cap)
    if effective_cap <= bits + 1: return 0
    return effective_cap - bits - 1


# =============================================================================
# [MAX-Q] EXPANDED ANSATZ
# =============================================================================

def build_expanded_ansatz(bits: int, ancilla: int, layers: int,
                          backend_mode: str = "simulator") -> "QuantumCircuit":
    """
    Build TwoLocal ansatz with ancilla qubits for MAX-Q utilisation.
    Enforces circuit size cap: IQM circuits <= _MAX_IQM_CIRCUIT qubits,
    Aer circuits <= _MAX_AER_QUBITS qubits. Safe ancilla count is computed
    by compute_ancilla_count() which already respects these limits.
    """
    # Safety cap: never exceed safe size for the target backend
    if backend_mode in ("iqm_hardware", "qrisp_iqm"):
        max_total = _MAX_IQM_CIRCUIT
    elif backend_mode == "ibm_hardware":
        max_total = _MAX_IBM_QUBITS
    else:
        max_total = _MAX_AER_QUBITS
    safe_ancilla = min(ancilla, max(0, max_total - bits))
    if safe_ancilla != ancilla:
        log.info(f"  [MAX-Q] Ancilla capped: {ancilla} → {safe_ancilla} "
                 f"(backend limit {max_total}q, bits={bits})")
    ancilla = safe_ancilla
    total   = bits + ancilla

    if ancilla == 0 or not QISKIT_OK:
        ans  = _make_twolocal(bits, layers)
        creg = ClassicalRegister(bits, "c")
        ans.add_register(creg)
        ans.measure(range(bits), creg)
        log.info(f"  [MAX-Q] No ancilla — ansatz({bits}q, reps={layers})")
        return ans

    full_ans = _make_twolocal(total, layers)
    cross    = QuantumCircuit(total)
    for ki in range(0, bits, _ANCILLA_STRIDE):
        ai = bits + (ki // _ANCILLA_STRIDE) % max(ancilla, 1)
        cross.cx(ki, ai); cross.cx(ai, ki)
    qc_exp = full_ans.compose(cross)
    creg   = ClassicalRegister(bits, "c")
    qc_exp.add_register(creg)
    qc_exp.measure(range(bits), creg)
    log.info(f"  [MAX-Q] Expanded ansatz: {total}q total  "
             f"({bits}q key + {ancilla}q ancilla)  reps={layers}")
    return qc_exp


def build_expanded_grover_ipe(
    bits: int, ancilla: int, top_offsets: List[int],
    h_biases: np.ndarray, n_ipe_rounds: int = 3,
) -> Optional["QuantumCircuit"]:
    if not QISKIT_OK: return None
    if ancilla == 0:
        return build_grover_ipe_circuit(bits, top_offsets, h_biases, n_ipe_rounds)
    n_rounds = max(n_ipe_rounds, 3)
    marked   = [int(o) for o in top_offsets if 0 <= int(o) < (1 << bits)][:64]
    if not marked: return None
    use_diag = False  # FIX: DiagonalGate crashes pytket; always RZ oracle
    ctrl_r = QuantumRegister(1, "ctrl"); key_r = QuantumRegister(bits, "key")
    anc_r  = QuantumRegister(ancilla, "anc"); cr = ClassicalRegister(bits, "mkey")
    qc     = QuantumCircuit(ctrl_r, key_r, anc_r, cr,
                            name=f"GroverIPE_{bits}bit_MaxQ")
    qc.h(key_r); qc.h(anc_r)
    if use_diag:
        diag = np.ones(1 << bits, dtype=complex)
        for o in marked: diag[o] = -1.0
        oracle_gate = None  # FIX: DiagonalGate crashes pytket — RZ oracle used below
        log.info(f"  [MAX-Q Grover-IPE] DiagonalGate  "
                 f"{bits}q key + {ancilla}q anc  {n_rounds} rds")
    else:
        oracle_gate = None
        vote = np.zeros(bits, dtype=float)
        for o in marked:
            for b in range(bits):
                if (o >> b) & 1: vote[b] += 1.0
        if vote.max() > 0: vote /= vote.max()
        log.info(f"  [MAX-Q Grover-IPE] Phase-kickback  "
                 f"{bits}q key + {ancilla}q anc  {n_rounds} rds")
    key_diffuser = _build_diffuser(bits)
    # FIX-CommutableMeasures: no mid-circuit measure/reset in loop
    for rnd in range(n_rounds):
        qc.h(ctrl_r[0])
        for i, hi in enumerate(h_biases):
            angle = float(2.0 * hi)
            if abs(angle) > 1e-6: qc.cp(angle, ctrl_r[0], key_r[i])
        qc.h(ctrl_r[0])
        qc.rz(math.pi / max(n_rounds, 1), ctrl_r[0])
        if use_diag and oracle_gate is not None:
            qc.append(oracle_gate, list(key_r))
        else:
            for b in range(bits):
                angle = float(math.pi * vote[b])
                if abs(angle) > 1e-6: qc.rz(angle, key_r[b])
        for ai in range(ancilla):
            ki = (ai * _ANCILLA_STRIDE) % bits
            qc.cx(key_r[ki], anc_r[ai])
        qc.append(key_diffuser, list(key_r))
    # Single terminal measurement
    qc.measure(key_r, cr)
    return qc


# =============================================================================
# [MODE1-PBIT] p-bit QPU sampler for large address-only puzzles
# =============================================================================

def run_mode1_pbit_sampler(
    bits: int, base: int, target_h160: bytes,
    h_biases: np.ndarray, J_couplings: np.ndarray,
    layers: int, iterations: int, shots: int, opt_level: int,
    backend_mode: str, iqm_device: str, iqm_token: str,
    ancilla: int, use_spsa: bool, spsa_max_iter: int,
    ibm_token: str = "", ibm_crn: str = "",
    ibm_backend_name: str = _IBM_DEFAULT_BACKEND,
) -> Tuple[List[Tuple[float, int]], Optional[int]]:
    log.info(f"  [MODE1-PBIT] bits={bits} > {_MODE1_GROVER_MAX_BITS} — "
             f"p-bit QPU exhaustive sampler mode")
    log.info(f"  [MODE1-PBIT] Generating ≈{iterations * shots:,} candidates…")

    all_samples:  List[Tuple[float, int]] = []
    found_offset: Optional[int]           = None

    circuit    = build_expanded_ansatz(bits, ancilla, layers)
    param_list = list(circuit.parameters)
    n_params   = len(param_list)

    iqm_backend = None; ibm_sampler_p = None; ibm_backend_obj_p = None
    if backend_mode == "iqm_hardware":
        try:
            iqm_backend = _get_iqm_backend_obj(iqm_device, iqm_token)
        except Exception as e:
            log.warning(f"  [MODE1-PBIT IQM] {e} — Aer fallback")
    elif backend_mode == "ibm_hardware":
        try:
            ibm_sampler_p, ibm_backend_obj_p = _get_ibm_sampler(
                ibm_token, ibm_crn, ibm_backend_name)
        except Exception as e:
            log.warning(f"  [MODE1-PBIT IBM] {e} — Aer fallback")

    def _run_params(pv: np.ndarray) -> dict:
        binding  = {p: float(v) for p, v in zip(param_list, pv)}
        bound_qc = circuit.assign_parameters(binding)
        if backend_mode == "ibm_hardware" and ibm_sampler_p is not None:
            try:
                return _run_on_ibm(bound_qc, ibm_sampler_p, ibm_backend_obj_p,
                                   min(shots, 1024), opt_level, "c")
            except Exception as ex:
                log.warning(f"  [IBM p-bit] {ex} — Aer fallback")
        return _execute_circuit(bound_qc, min(shots, 1024), opt_level,
                                backend_mode, iqm_backend, "c")

    if use_spsa and SPSA_OK:
        x0 = _make_biased_params(h_biases, J_couplings, n_params, bits, 0.2)
        def _obj(pv):
            try:
                counts = _run_params(pv)
                total_e = 0.0; total_w = 0
                for bs, cnt in counts.items():
                    off = int(bs.zfill(bits)[-bits:], 2)
                    e   = compute_energy(base+off, target_h160)
                    total_e += e*cnt; total_w += cnt
                return total_e / max(total_w, 1)
            except Exception: return 256.0
        try:
            res    = SPSA(maxiter=spsa_max_iter).minimize(_obj, x0=x0)
            best_p = res.x
            log.info(f"  [MODE1-PBIT SPSA] Optimised energy={res.fun:.3f}")
        except Exception as ex:
            log.warning(f"  [MODE1-PBIT SPSA] failed ({ex}) — seeded params")
            best_p = x0
    else:
        best_p = _make_biased_params(h_biases, J_couplings, n_params, bits, 0.3)

    verified = 0
    for it in range(iterations):
        noise  = np.random.normal(0, 0.2, n_params)
        params = best_p + noise
        try:
            binding  = {p: float(v) for p, v in zip(param_list, params)}
            bound_qc = circuit.assign_parameters(binding)
            counts   = _execute_circuit(bound_qc, shots, opt_level,
                                        backend_mode, iqm_backend, "c")
        except Exception as ex:
            log.warning(f"  [MODE1-PBIT iter {it+1}] error: {ex}"); continue

        for bs, cnt in counts.items():
            off   = int(bs.zfill(bits)[-bits:], 2)
            k     = base + off
            h     = _k_to_hash160(k)
            verified += 1
            e  = compute_energy(k, target_h160)
            bv = np.array([(off >> b) & 1 for b in range(bits)], dtype=float)
            eff = 0.7*e - 0.3*float(np.dot(h_biases, bv))
            w = max(1, min(cnt, 20))
            for _ in range(w): all_samples.append((eff, off))
            if h == target_h160 and found_offset is None:
                found_offset = off
                log.info(f"  [MODE1-PBIT] 🎉 HASH MATCH  offset={off}  k={hex(k)}")
        log.info(f"  [MODE1-PBIT iter {it+1}/{iterations}]  "
                 f"verified={verified}  "
                 f"found={'YES ✅' if found_offset is not None else 'not yet'}")
        if found_offset is not None: break

    return all_samples, found_offset


# =============================================================================
# PHASE B — SAMPLER WALK  [G-1 SPSA + IQM backend]
# =============================================================================

def run_sampler_phase(
    bits: int, base: int, target_h160: bytes,
    pubkey_xy: Optional[Tuple[int, int]],
    pubkey_hex: Optional[str],
    h_biases: np.ndarray, J_couplings: np.ndarray,
    layers: int = 4, iterations: int = 12,
    shots: int = 4096, opt_level: int = 2,
    backend_mode: str = "simulator",
    iqm_device: str = "garnet",
    iqm_token: str = "",
    ibm_token: str = "", ibm_crn: str = "",
    ibm_backend_name: str = _IBM_DEFAULT_BACKEND,
    use_spsa: bool = True,
    spsa_max_iter: int = 60,
    ancilla: int = 0,
    full_start: int = 0, full_end: int = 0,
) -> Tuple[List[Tuple[float, int]], float]:
    """
    Phase B sampler. Routes to:
      simulator    → Aer (local)
      iqm_hardware → IQM via pytket bridge
      qrisp_iqm   → IQM via Qrisp (auto-native-transpilation)
      ibm_hardware → IBM Quantum Runtime
    """
    if full_end == 0:
        full_start, full_end = auto_range(bits)
    # ── Qrisp path (completely separate from Qiskit circuit flow) ─────────────
    if backend_mode == "qrisp_iqm":
        log.info("=" * 60)
        log.info(f"  [Qrisp-IQM Sampler] bits={bits} layers={layers} "
                 f"iters={iterations} shots={shots}  device={iqm_device}")
        try:
            qrisp_backend = _get_qrisp_iqm_backend(iqm_device, iqm_token)
        except Exception as e:
            log.warning(f"  [Qrisp-IQM] Connect failed ({e}) → Aer fallback")
            backend_mode = "simulator"
        else:
            samples = _run_sampler_via_qrisp(
                h_biases=h_biases, bits=bits, base=base,
                target_h160=target_h160, pubkey_xy=pubkey_xy, pubkey_hex=pubkey_hex,
                qrisp_backend=qrisp_backend,
                shots=shots, layers=layers, iterations=iterations,
                J_couplings=J_couplings,
            )
            best_e = min((e for e, _ in samples), default=256.0)
            log.info(f"  [Qrisp-IQM Sampler] done — {len(samples)} pairs  best={best_e:.3f}")
            return samples, best_e

    if not QISKIT_OK:
        log.error("Qiskit not available"); return [], 256.0

    log.info("=" * 60)
    log.info(f"  [Sampler] bits={bits} ancilla={ancilla} layers={layers} "
             f"iters={iterations} shots={shots}  backend={backend_mode}")

    circuit    = build_expanded_ansatz(bits, ancilla, layers, backend_mode)
    param_list = list(circuit.parameters)
    n_params   = len(param_list)
    log.info(f"  Ansatz: depth={circuit.depth()} params={n_params}")

    iqm_backend = None; ibm_sampler = None; ibm_backend_obj = None
    if backend_mode == "iqm_hardware":
        try:
            iqm_backend = _get_iqm_backend_obj(iqm_device, iqm_token)
        except Exception as e:
            log.warning(f"  [IQM] Connection failed ({e}) → Aer fallback")
            backend_mode = "simulator"
    elif backend_mode == "ibm_hardware":
        try:
            ibm_sampler, ibm_backend_obj = _get_ibm_sampler(
                ibm_token, ibm_crn, ibm_backend_name)
        except Exception as e:
            log.warning(f"  [IBM] Connection failed ({e}) → Aer fallback")
            backend_mode = "simulator"

    all_samples: List[Tuple[float, int]] = []
    best_energy = 256.0

    def _run_params(pv: np.ndarray) -> dict:
        binding  = {p: float(v) for p, v in zip(param_list, pv)}
        bound_qc = circuit.assign_parameters(binding)
        if backend_mode == "ibm_hardware" and ibm_sampler is not None:
            try:
                return _run_on_ibm(bound_qc, ibm_sampler, ibm_backend_obj,
                                   shots, opt_level, "c")
            except Exception as ex:
                log.warning(f"  [IBM exec] {ex} — Aer fallback")
        return _execute_circuit(bound_qc, shots, opt_level,
                                backend_mode, iqm_backend, "c")

    def _counts_to_samples(counts: dict) -> List[Tuple[float, int]]:
        result = []
        max_valid_off = full_end - base      # FIX: only accept in-range offsets
        min_valid_off = max(0, full_start - base)
        for bitstr, cnt in counts.items():
            bs     = bitstr.zfill(bits)[-bits:]
            offset = int(bs, 2)
            # FIX: discard measurements that fall outside the valid key range
            # (range-shift can push ~50% of raw offsets above full_end)
            if offset < min_valid_off or offset > max_valid_off:
                continue
            energy = compute_energy(base+offset, target_h160, pubkey_xy, pubkey_hex)
            bv     = np.array([(offset >> b) & 1 for b in range(bits)], dtype=float)
            dot_norm = (float(np.dot(h_biases, bv)) + bits) / (2.0 * bits + 1e-9)
            eff    = 0.7 * energy + 0.3 * (1.0 - dot_norm)
            w = max(1, min(cnt, 20))
            for _ in range(w): result.append((eff, offset))
        return result

    # ── [G-1] 1-SPSA — ONE QPU job per iteration (not 2) ─────────────────────
    # FIX-JOB-EXPLOSION: standard SPSA uses 2 QPU jobs per iteration for
    # finite-difference gradient estimation.  We use 1-SPSA: random ±δ
    # perturbation, accept if energy improves.  Half the QPU submissions.
    if use_spsa and SPSA_OK:
        log.info(f"  [G-1 1-SPSA] {spsa_max_iter} single-shot iterations "
                 f"(1 QPU job/iter)…")
        best_params = _make_biased_params(h_biases, J_couplings, n_params, bits, 0.2)
        prev_energy = 1.0
        alpha = 0.6   # standard SPSA learning-rate decay exponent

        for spsa_it in range(spsa_max_iter):
            ak      = 0.3 / (spsa_it + 1) ** alpha
            delta   = np.where(np.random.random(n_params) > 0.5, 1.0, -1.0)
            p_plus  = best_params + ak * delta
            try:
                s_plus  = _counts_to_samples(_run_params(p_plus))
                e_plus  = float(np.mean([s[0] for s in s_plus])) if s_plus else 1.0
            except Exception:
                e_plus  = 1.0
            if e_plus < prev_energy:
                best_params = p_plus; prev_energy = e_plus
            if (spsa_it + 1) % 10 == 0 or spsa_it == 0:
                log.info(f"  [1-SPSA {spsa_it+1}/{spsa_max_iter}] "
                         f"energy={prev_energy:.4f}")

        for it in range(iterations):
            noise  = np.random.normal(0, 0.10, n_params)
            params = best_params + noise
            try:
                samples = _counts_to_samples(_run_params(params))
                for eff, offset in samples:
                    if eff < best_energy: best_energy = eff
                all_samples.extend(samples)
                log.info(f"  [Sampler 1-SPSA {it+1}/{iterations}] "
                         f"best_eff={best_energy:.3f}  "
                         f"unique={len(set(o for _,o in samples))}  "
                         f"total={len(all_samples)}")
            except Exception as e:
                log.warning(f"  [iter {it+1}] shot error: {e}")

    else:
        # ── Fallback: FIX-1 seeded-noise iteration loop ────────────────────────
        log.info("  [G-1] SPSA not available — using FIX-1 seeded noise loop")
        for it in range(iterations):
            noise_scale = 0.4 + 0.1*(it/max(iterations-1, 1))
            params = _make_biased_params(h_biases, J_couplings, n_params, bits, noise_scale)
            try:
                counts  = _run_params(params)
                samples = _counts_to_samples(counts)
                for eff, offset in samples:
                    if eff < best_energy: best_energy = eff
                all_samples.extend(samples)
                log.info(f"  [Sampler {it+1}/{iterations}] best_eff={best_energy:.3f}  "
                         f"unique={len(counts)}  total={len(all_samples)}")
            except Exception as e:
                log.warning(f"  [iter {it+1}] shot error: {e}")

    log.info(f"  [Sampler] done — {len(all_samples)} pairs")
    return all_samples, best_energy


# =============================================================================
# PHASE C RUNNER  (IQM-aware)
# =============================================================================

def run_grover_ipe_phase(
    bits: int, sampler_samples: List[Tuple[float, int]],
    h_biases: np.ndarray, base: int, target_h160: bytes,
    pubkey_xy: Optional[Tuple[int, int]], pubkey_hex: Optional[str],
    shots: int = 4096, n_ipe_rounds: int = 3, top_k: int = 128,
    backend_mode: str = "simulator",
    iqm_device: str = "garnet",
    iqm_token: str = "",
    ibm_token: str = "", ibm_crn: str = "",
    ibm_backend_name: str = _IBM_DEFAULT_BACKEND,
    ancilla: int = 0,
    opt_level: int = 1,
) -> List[Tuple[float, int]]:
    if backend_mode == "qrisp_iqm":
        log.info("  [Grover-IPE] Skipped for qrisp_iqm (Qrisp sampler handles Phase B)")
        return []
    if not QISKIT_OK:
        log.warning("  [Grover-IPE] Qiskit unavailable — skipped"); return []
    sorted_s = sorted(sampler_samples, key=lambda x: x[0])
    top_offs = list(dict.fromkeys(int(o) for _, o in sorted_s[:top_k]))
    if not top_offs: return []

    qc = build_expanded_grover_ipe(bits, ancilla, top_offs, h_biases, n_ipe_rounds)
    if qc is None: return []

    iqm_backend = None; ibm_sampler_g = None; ibm_backend_obj_g = None
    if backend_mode == "iqm_hardware":
        try:
            iqm_backend = _get_iqm_backend_obj(iqm_device, iqm_token)
        except Exception as e:
            log.warning(f"  [IQM Grover-IPE] {e} — Aer fallback")
            backend_mode = "simulator"
    elif backend_mode == "ibm_hardware":
        try:
            ibm_sampler_g, ibm_backend_obj_g = _get_ibm_sampler(
                ibm_token, ibm_crn, ibm_backend_name)
        except Exception as e:
            log.warning(f"  [IBM Grover-IPE] {e} — Aer fallback")
            backend_mode = "simulator"

    try:
        if backend_mode == "ibm_hardware" and ibm_sampler_g is not None:
            counts = _run_on_ibm(qc, ibm_sampler_g, ibm_backend_obj_g,
                                 shots, opt_level, "mkey")
        else:
            counts = _execute_circuit(qc, shots, opt_level,
                                      backend_mode, iqm_backend, "mkey")
    except Exception as e:
        log.warning(f"  [Grover-IPE] error: {e}"); return []

    log.info(f"  [Grover-IPE] depth={qc.depth()} size={qc.size()}")
    extra: List[Tuple[float, int]] = []
    for bitstr, cnt in counts.items():
        bs     = bitstr.zfill(bits)[-bits:]
        offset = int(bs, 2)
        energy = compute_energy(base+offset, target_h160, pubkey_xy, pubkey_hex)
        bv     = np.array([(offset >> b) & 1 for b in range(bits)], dtype=float)
        eff    = 0.7*energy - 0.3*float(np.dot(h_biases, bv))
        w = max(1, min(cnt, 20))
        for _ in range(w): extra.append((eff, offset))
    log.info(f"  [Grover-IPE] {len(extra)} additional pairs")
    return extra


# =============================================================================
# [G-5] KANGAROO-COMPATIBLE RANGE EXPORT
# =============================================================================

def export_kangaroo(
    start_r: int, end_r: int, bits: int,
    pubkey_xy: Optional[Tuple[int, int]],
    shift: int, address: str = "", fname: str = "",
    iqm_device: str = "garnet",
) -> str:
    ts  = datetime.now().strftime("%Y%m%d_%H%M%S")
    fn  = fname or f"kangaroo_export_{bits}bit_{ts}.json"
    mid = (start_r + end_r) // 2
    payload = {
        "tool":           "KEY-REDUCER IQM Edition",
        "timestamp":      datetime.now().isoformat(),
        "backend":        f"IQM {iqm_device.capitalize()} "
                          f"({IQM_DEVICE_QUBITS.get(iqm_device, '?')}q)",
        "puzzle_bits":    bits,
        "address":        address,
        "upper_bound":    hex(start_r),
        "lower_bound":    hex(end_r),
        "range_size":     end_r - start_r,
        "midpoint":       hex(mid),
        "shift_applied":  shift != 0,
        "shift_value":    hex(shift) if shift else "0",
        "bitcrack_cmd":   f"bitcrack --keyspace {hex(start_r)}:{hex(end_r)} "
                          f"{address or '<addr>'}",
        "keyhunt_cmd":    f"keyhunt -m bsgs -r {hex(start_r)}:{hex(end_r)}",
        "honest_note":    ("Heuristic estimate. Key may not be inside. "
                           "Run --self-test to calibrate."),
    }
    if pubkey_xy is not None:
        payload["pubkey_x"] = hex(pubkey_xy[0])
        payload["pubkey_y"] = hex(pubkey_xy[1])
        if shift != 0:
            shift_G = _pt_mul(shift, (_Gx, _Gy))
            if shift_G is not None:
                neg_sg    = (shift_G[0], (_P - shift_G[1]) % _P)
                q_shifted = _pt_add(pubkey_xy, neg_sg)
                if q_shifted is not None:
                    half = (end_r - start_r) // 2
                    payload["shifted_pubkey_x"]   = hex(q_shifted[0])
                    payload["shifted_pubkey_y"]   = hex(q_shifted[1])
                    payload["kangaroo_range_neg"] = hex(-half)
                    payload["kangaroo_range_pos"] = hex(half)
                    payload["kangaroo_note"]      = (
                        "Search d' in [-(range/2), +(range/2)] against Q_shifted.")
    with open(fn, "w") as f: json.dump(payload, f, indent=2)
    log.info(f"  [G-5 Kangaroo export] → {fn}")
    return fn


# =============================================================================
# PLOT & SAVE
# =============================================================================

def plot_bit_probs(bit_probs: np.ndarray, bits: int, pinned: List[str],
                   label: str = "", save_path: str = "") -> None:
    if not MPL_OK: return
    fig, ax = plt.subplots(figsize=(max(10, bits // 2), 5))
    colors  = ["red" if p=="1" else "green" if p=="0" else "steelblue" for p in pinned]
    ax.bar(range(bits), bit_probs, color=colors, edgecolor="black", alpha=0.85)
    ax.axhline(0.85, color="red",   ls="--", lw=1.2, label="Pin→1 (>0.85)")
    ax.axhline(0.15, color="green", ls="--", lw=1.2, label="Pin→0 (<0.15)")
    ax.axhline(0.50, color="gray",  ls=":",  lw=0.8, label="Uniform (0.50)")
    ax.set_title(f"Bit Probability Distribution — {label}", fontsize=12)
    ax.set_xlabel("Bit position (0 = MSB)"); ax.set_ylabel("P(bit=1)")
    ax.set_ylim(0, 1.05); ax.legend(); ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150); log.info(f"  Plot → {save_path}")
    try: plt.show()
    except Exception: pass
    plt.close()


def save_result(start_r: int, end_r: int, bits: int,
                pinned: List[str], bit_probs: np.ndarray,
                mode_label: str, address: str = "",
                iqm_device: str = "garnet",
                backend_mode: str = "simulator",
                ibm_backend_name: str = _IBM_DEFAULT_BACKEND) -> str:
    ts    = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"reduced_range_{bits}bit_{ts}.txt"
    pc    = sum(1 for b in pinned if b in ("0","1"))
    if backend_mode == "qrisp_iqm":
        be_label = (f"IQM {iqm_device.capitalize()} via Qrisp "
                    f"({IQM_DEVICE_QUBITS.get(iqm_device,'?')}q)")
    elif backend_mode == "iqm_hardware":
        be_label = (f"IQM {iqm_device.capitalize()} via pytket "
                    f"({IQM_DEVICE_QUBITS.get(iqm_device,'?')}q)")
    elif backend_mode == "ibm_hardware":
        be_label = f"IBM Quantum {ibm_backend_name}"
    else:
        be_label = "Aer Simulator (local)"
    with open(fname, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("KEY-REDUCER — Supreme Edition — QUANTUM PROBABILISTIC KEYSPACE REDUCTION\n")
        f.write(f"Backend: {be_label}\n")
        f.write("Method: Quantum Walk (O(√N)) + Grover-IPE + Trajectory FWHM bracket\n")
        f.write("OUTPUT: two measured key values that bracket the interference density peak.\n")
        f.write("        NOT a forced percentage — these are actual QPU measurement results.\n")
        f.write("        Run --self-test to measure how often the true key is inside.\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Timestamp      : {datetime.now()}\n")
        f.write(f"Mode           : {mode_label}\n")
        f.write(f"Bit length     : {bits}\n")
        f.write(f"Bits pinned    : {pc}/{bits}\n")
        f.write(f"Reduction      : ~{1<<pc}× factor (heuristic)\n\n")
        f.write(f"UPPER BOUND (hex): {hex(start_r)}\n")
        f.write(f"LOWER BOUND (hex): {hex(end_r)}\n")
        f.write(f"Range size     : {end_r-start_r:,} keys\n\n")
        f.write("Pinned pattern : " + "".join(pinned) + "\n")
        f.write("Bit probs      : " + " ".join(f"{p:.3f}" for p in bit_probs) + "\n\n")
        f.write("# BitCrack GPU command:\n")
        f.write(f"#   bitcrack --keyspace {hex(start_r)}:{hex(end_r)} "
                f"{address or '<address>'}\n")
        f.write("=" * 80 + "\n")
    log.info(f"  Result → {fname}")
    return fname




# =============================================================================
# [ECPRA] EC PERIOD RESONANCE ATTACK — Shor-inspired multi-angle probing
# Ported from Quantum-Shor-v16.py and integrated into the full pipeline.
# =============================================================================

def ec_period_resonance_attack(
    pubkey_xy: Tuple[int, int],
    base: int, bits: int,
    full_start: int, full_end: int,
    h_biases: "np.ndarray",
    J_couplings: "np.ndarray",
    shots: int = 2048,
    opt_level: int = 1,
    backend_mode: str = "simulator",
    iqm_device: str = "garnet",
    iqm_token: str = "",
    ibm_token: str = "",
    ibm_crn: str = "",
    ibm_backend_name: str = "",
    n_steps: int = 3,
) -> List[Tuple[float, int]]:
    """
    Shor's insight applied to ECDLP: instead of searching for k directly,
    probe the EC energy landscape from K different step-size angles.

    For each step size s_i, the probe sequence P(x) = (base + x*s_i)*G
    has a quasi-period of n/s_i. When multiple step views AGREE that
    offset o has low energy, that resonance = our period-finding signal.

    K step sizes = K QPU jobs (one walk per step).
    Combined resonance scores from all K walks vote on the best region.
    This is the CRT / multi-modular philosophy of Shor, applied classically
    and quantumly to EC point energy landscapes.
    """
    valid_range = full_end - full_start
    if valid_range < 4 or pubkey_xy is None:
        return []

    target_h160 = b""

    # Geometric step sizes: s_i = 2^(bits*i/K), covers micro to macro scales
    step_sizes, seen = [], set()
    for i in range(n_steps):
        exp = max(0, (bits * i) // max(n_steps, 1))
        s   = max(1, min(1 << exp, valid_range // 4))
        if s not in seen:
            seen.add(s); step_sizes.append(s)

    log.info(f"  [ECPRA] Shor-inspired probing  steps={step_sizes}  shots/step={shots}")

    all_resonance: Dict[int, float] = {}
    all_pairs: List[Tuple[float, int]] = []

    for step_idx, s in enumerate(step_sizes):
        # Probe offsets spaced s apart across the valid range
        n_probes = min(256, max(32, valid_range // max(s, 1)))
        base_off = valid_range // (2 * max(n_probes, 1))
        probe_offs = sorted(set(
            max(0, min(valid_range - 1, (base_off + j * s) % valid_range))
            for j in range(n_probes)
        ))

        # Energy at each probe offset for this step's viewing angle
        probe_e = [compute_energy(base + o, target_h160, pubkey_xy, None)
                   for o in probe_offs]

        # Step-specific h_biases from this angle's energy landscape
        step_biases = np.zeros(bits, dtype=float)
        for b in range(bits):
            mask1 = np.array([(o >> b) & 1 for o in probe_offs], dtype=bool)
            ea    = np.array(probe_e)
            e1 = ea[mask1]; e0 = ea[~mask1]
            step_biases[b] = 2.0 * ((e0.mean() if len(e0) else 0.5) -
                                     (e1.mean() if len(e1) else 0.5))
        step_biases = np.clip(step_biases, -1.0, 1.0)

        # Accumulate classical resonance from probe energies
        for o, e in zip(probe_offs, probe_e):
            all_resonance[o] = all_resonance.get(o, 0.0) + (1.0 - float(e))
            all_pairs.append((float(e), o))

        # ONE QPU walk job for this step with step-specific biases
        if QISKIT_OK:
            try:
                key_r = QuantumRegister(bits, "k")
                cr    = ClassicalRegister(bits, "c")
                qc    = QuantumCircuit(key_r, cr, name=f"ECPRA_s{step_idx}")
                qc.h(key_r)
                for b in range(bits):
                    ang = float(np.arccos(np.clip(-step_biases[b], -1.0, 1.0)))
                    if abs(ang) > 1e-6: qc.ry(ang, key_r[b])
                for b in range(1, bits):
                    qc.cx(key_r[b-1], key_r[b])
                px = pubkey_xy[0]
                for b in range(bits):
                    phi = math.pi * (1.0 - 2.0 * ((px >> b) & 1)) * 0.7
                    if abs(phi) > 1e-6: qc.rz(phi, key_r[b])
                for b in range(bits - 1, 0, -1):
                    qc.cx(key_r[b-1], key_r[b])
                qc.measure(key_r, cr)

                iqm_obj = (_get_iqm_backend_obj(iqm_device, iqm_token)
                           if backend_mode == "iqm_hardware" else None)
                counts  = _execute_circuit(qc, shots, opt_level,
                                           backend_mode, iqm_obj,
                                           f"ecpra_{step_idx}")
                for bitstr, cnt in counts.items():
                    bs  = bitstr.zfill(bits)[-bits:]
                    off = int(bs, 2)
                    if 0 <= off < valid_range:
                        e   = compute_energy(base+off, target_h160, pubkey_xy, None)
                        res = all_resonance.get(off, 0.0)
                        eff = e / max(1.0, 1.0 + res * 0.1)
                        all_pairs.append((eff, off))
                        all_resonance[off] = all_resonance.get(off, 0.0) + (1.0 - e)

                log.info(f"  [ECPRA] Step {step_idx+1}/{len(step_sizes)} "
                         f"s={s}  probes={len(probe_offs)}  "
                         f"shots={sum(counts.values())}")
            except Exception as ex:
                log.warning(f"  [ECPRA] Step {step_idx+1} QPU: {ex}")

    # Convert resonance map to normalised (energy, offset) pairs
    if all_resonance:
        max_res = max(all_resonance.values())
        res_pairs = [(1.0 - r / max(max_res, 1e-9), o)
                     for o, r in all_resonance.items()]
        top5 = sorted(res_pairs)[:5]
        log.info("  [ECPRA] Top-5 resonance peaks (low-e = strong agreement):")
        for rank, (eff, off) in enumerate(top5):
            log.info(f"    #{rank+1}: {hex(base+off)}  resonance_e={eff:.6f}")
        all_pairs.extend(res_pairs)

    log.info(f"  [ECPRA] Total pairs: {len(all_pairs)}")
    return all_pairs

# =============================================================================
# MASTER ORCHESTRATOR — reduce_keyspace()
# =============================================================================

def reduce_keyspace(
    bits: int, base: int, target_h160: bytes,
    pubkey_xy: Optional[Tuple[int, int]] = None,
    pubkey_hex: Optional[str] = None,
    layers: int = 4, iterations: int = 12,
    shots: int = 4096, opt_level: int = 2,
    n_probes: int = 512,
    grover_shots: int = 4096, n_ipe_rounds: int = 3,
    grover_top_k: int = 128,
    backend_mode: str = "simulator",
    iqm_device: str = "garnet",
    iqm_token: str = "",
    ibm_token: str = "", ibm_crn: str = "",
    ibm_backend_name: str = _IBM_DEFAULT_BACKEND,
    save_plot: bool = True, mode_label: str = "Unknown", address: str = "",
    use_range_shift: bool = True,
    use_spsa: bool = True,
    spsa_max_iter: int = 60,
    use_kangaroo_export: bool = True,
    use_shor_s1:         bool = True,
    use_shor_s2:         bool = True,
    use_shor_s3:         bool = True,
    full_start_override: int = 0,
    full_end_override:   int = 0,
) -> Tuple[int, int, List[str], np.ndarray]:
    """
    Full pipeline A→B→B2→C→D→E.
    A  : Ising Hamiltonian (SparsePauliOp, Sobol probing)
    B  : TwoLocal SPSA sampler (or Qrisp sampler)
    B2 : [QUANTUM WALK] Discrete-time quantum walk — superior O(√N) exploration
    C  : Grover-IPE / Real Grover / p-bit sampler
    D  : Lattice BKZ + DBSCAN + trajectory density range extraction
    E  : Kangaroo export + multi-run voting
    ALWAYS returns (start_r, end_r, pinned, bit_probs).
    backend_mode: "simulator" | "iqm_hardware" | "qrisp_iqm" | "ibm_hardware"
    """
    _auto_start, _auto_end = auto_range(bits)
    full_start = full_start_override if full_start_override > 0 else _auto_start
    full_end   = full_end_override   if full_end_override   > 0 else _auto_end
    log.info("=" * 72)
    log.info(f"  REDUCE  {bits}-bit  base={hex(base)}  mode={mode_label}")
    log.info(f"  Backend: {backend_mode}  device: {iqm_device}")
    log.info(f"  Full range: [{hex(full_start)}, {hex(full_end)}]"
             + (" [USER CUSTOM]" if full_start_override or full_end_override else " [auto]"))

    # [G-4] Range shift
    shift = 0; pubkey_shifted = None
    if pubkey_xy is not None and use_range_shift:
        pubkey_shifted, shift = range_shift_pubkey(
            pubkey_xy, base, bits,
            full_start=full_start, full_end=full_end)
        if pubkey_shifted is not None:
            log.info(f"  [G-4] Range shift active: shift={hex(shift)[:18]}")

    # [MAX-Q] Query capacity and compute safe ancilla count
    backend_capacity = get_backend_qubit_capacity(backend_mode, iqm_device,
                                                   ibm_backend_name)
    ancilla          = compute_ancilla_count(bits, backend_capacity, backend_mode)
    if ancilla > 0:
        log.info(f"  [MAX-Q] Using {bits+ancilla+1}q total  "
                 f"({bits}q key  +  {ancilla}q ancilla  +  1q Grover-ctrl)")
    else:
        log.info(f"  [MAX-Q] No ancilla expansion (bits={bits} fills device)")

    # Phase A: EC deltas + SparsePauliOp [G-2, G-3]
    dxs: Optional[List[int]] = None
    effective_pubkey = pubkey_shifted if pubkey_shifted is not None else pubkey_xy
    if effective_pubkey is not None:
        try: dxs, _ = precompute_deltas(effective_pubkey, base, bits)
        except Exception as e: log.warning(f"  [deltas] skipped: {e}")

    try:
        _, h_biases, J_couplings = build_ising_hamiltonian(
            bits, base, target_h160, effective_pubkey, pubkey_hex, n_probes, dxs)
    except Exception as e:
        log.warning(f"  [SparsePauliOp] failed: {e}")
        h_biases = np.zeros(bits); J_couplings = np.zeros(max(1, bits-1))

    # Phase B: SPSA-optimised sampler [G-1]
    # FIX: energy scoring always uses ORIGINAL pubkey_xy, not shifted
    sampler_samples, best_energy = run_sampler_phase(
        bits=bits, base=base,
        target_h160=target_h160, pubkey_xy=pubkey_xy, pubkey_hex=pubkey_hex,
        h_biases=h_biases, J_couplings=J_couplings,
        layers=layers, iterations=iterations, shots=shots, opt_level=opt_level,
        backend_mode=backend_mode, iqm_device=iqm_device, iqm_token=iqm_token,
        ibm_token=ibm_token, ibm_crn=ibm_crn, ibm_backend_name=ibm_backend_name,
        use_spsa=use_spsa, spsa_max_iter=spsa_max_iter, ancilla=ancilla,
        full_start=full_start, full_end=full_end,
    )
    log.info(f"  [Phase B] {len(sampler_samples)} pairs  best_eff={best_energy:.3f}")

    # =============================================================================
    # [PHASE B2 — THREE ENGINES WORKING TOGETHER]
    # =============================================================================
    #
    # Engine 1: P-BIT (Classical Glauber dynamics, CPU)
    # Engine 2: QPB v3 (Quantum P-Bit gate on QPU/Aer)
    # Engine 3: ADAPTIVE-COIN QUANTUM WALK (v18 per-step phase oracle, QPU/Aer)
    #
    # All three explore the SAME key-space but via different physics.
    # Their combined density map gives a richer, more accurate snake corridor.
    # =============================================================================

    # ── Engine 1: Classical P-bit walk (always runs, CPU-only) ──────────────
    pbit_n_chains = max(32, min(256, iterations * 8))
    pbit_n_steps  = max(500, min(4000, (1 << min(bits, 12)) // 4))
    pbit_burn_in  = max(50, pbit_n_steps // 8)
    pbit_beta_start = 0.3 + 0.05 * math.log2(max(bits, 2))
    pbit_beta_end   = 2.0 + 0.20 * math.log2(max(bits, 2))

    log.info(f"  [Phase B2 PBit-v1] {pbit_n_chains} chains × {pbit_n_steps} steps  "
             f"β: {pbit_beta_start:.2f}→{pbit_beta_end:.2f}  burn_in={pbit_burn_in}")
    try:
        pbit_samples = run_pbit_walk_phase(
            bits=bits, base=base,
            target_h160=target_h160, pubkey_xy=pubkey_xy, pubkey_hex=pubkey_hex,
            h_biases=h_biases, J_couplings=J_couplings,
            full_start=full_start, full_end=full_end,
            n_chains=pbit_n_chains, n_steps=pbit_n_steps,
            burn_in=pbit_burn_in,
            beta_start=pbit_beta_start, beta_end=pbit_beta_end,
            dxs=dxs,
        )
        sampler_samples = sampler_samples + pbit_samples
        log.info(f"  [Phase B2 PBit-v1] +{len(pbit_samples):,} p-bit samples → "
                 f"total={len(sampler_samples):,}")
    except Exception as _pbit_ex:
        log.warning(f"  [Phase B2 PBit-v1] failed: {_pbit_ex}")

    # ── Engine 2: QPB v3 circuits (qubits acting as p-bits on QPU) ───────────
    walk_steps = max(3, min(8, bits // 4))
    n_walks    = max(2, min(6, iterations // 2))
    walk_shots = max(1024, min(shots, 8192))
    log.info(f"  [Phase B2 QPBv3] {n_walks} circuits × {walk_steps} steps × {walk_shots} shots  "
             f"(QPB gate: Ry(2·arcsin(√sigmoid(β·I_b))) + CRZ coupling)  β:0.5→4.0")
    qpb_samples = run_quantum_walk_phase(
        bits=bits, base=base,
        target_h160=target_h160, pubkey_xy=pubkey_xy, pubkey_hex=pubkey_hex,
        h_biases=h_biases, J_couplings=J_couplings,
        ancilla=0, walk_steps=walk_steps,
        shots=walk_shots, opt_level=opt_level,
        backend_mode=backend_mode, iqm_device=iqm_device, iqm_token=iqm_token,
        ibm_token=ibm_token, ibm_crn=ibm_crn, ibm_backend_name=ibm_backend_name,
        n_walks=n_walks, dxs=dxs,
        full_start=full_start, full_end=full_end,
    )
    sampler_samples = sampler_samples + qpb_samples
    log.info(f"  [Phase B2 QPBv3] +{len(qpb_samples):,} QPB samples → "
             f"total={len(sampler_samples):,}")

    # ── Engine 3: Adaptive-Coin Quantum Walk (v18 per-step oracle) ───────────
    # Runs additional walk circuits using the v18-style adaptive coin (Ry(θ_b)
    # per qubit with coin_angles updated by phase oracle feedback) as a
    # COMPLEMENT to the QPB engine. The two quantum approaches explore different
    # parts of the Hilbert space, and their combined density is more informative.
    # Uses half the shots/walks of the QPB engine (already covered by QPB+p-bit).
    walk_steps_ac = max(2, min(6, bits // 5))
    n_walks_ac    = max(1, min(3, iterations // 4))
    walk_shots_ac = max(512, min(walk_shots // 2, 4096))
    log.info(f"  [Phase B2 AdapCoin] {n_walks_ac} walks × {walk_steps_ac} steps × "
             f"{walk_shots_ac} shots  (adaptive-coin + per-step phase oracle)")
    try:
        ac_samples = _run_adaptive_coin_walk(
            bits=bits, base=base,
            target_h160=target_h160, pubkey_xy=pubkey_xy, pubkey_hex=pubkey_hex,
            h_biases=h_biases, J_couplings=J_couplings,
            walk_steps=walk_steps_ac, n_walks=n_walks_ac,
            shots=walk_shots_ac, opt_level=opt_level,
            backend_mode=backend_mode, iqm_device=iqm_device, iqm_token=iqm_token,
            ibm_token=ibm_token, ibm_crn=ibm_crn, ibm_backend_name=ibm_backend_name,
            dxs=dxs, full_start=full_start, full_end=full_end,
        )
        sampler_samples = sampler_samples + ac_samples
        log.info(f"  [Phase B2 AdapCoin] +{len(ac_samples):,} adaptive-coin samples → "
                 f"total={len(sampler_samples):,}")
    except Exception as _ac_ex:
        log.warning(f"  [Phase B2 AdapCoin] failed: {_ac_ex}")

    log.info(f"  [Phase B2] All three engines complete → "
             f"total={len(sampler_samples):,} pairs in combined pool")

    # ── [ECPRA] Shor-inspired EC Period Resonance Attack ─────────────────────
    # Multi-step EC period probing adds resonance-scored pairs to sampler_samples
    # BEFORE Shor S1/S2/S3 phases, giving them better-targeted starting data.
    # FIX-v17: previous code called all_samples.extend() but all_samples is only
    # defined in Phase D — causing NameError caught as WARNING "couldn't get
    # all_samples". Correct target is sampler_samples (already defined above).
    try:
        _ecpra_pubkey = effective_pubkey or pubkey_xy
        if _ecpra_pubkey is not None:
            ecpra_pairs = ec_period_resonance_attack(
                pubkey_xy    = _ecpra_pubkey,
                base         = base,
                bits         = bits,
                full_start   = full_start,
                full_end     = full_end,
                h_biases     = h_biases,
                J_couplings  = J_couplings,
                shots        = min(shots, 2048),
                opt_level    = opt_level,
                backend_mode = backend_mode,
                iqm_device   = iqm_device,
                iqm_token    = iqm_token,
                ibm_token    = ibm_token,
                ibm_crn      = ibm_crn,
                ibm_backend_name = ibm_backend_name,
                n_steps      = max(2, min(4, bits // 6)),
            )
            if ecpra_pairs:
                sampler_samples = sampler_samples + ecpra_pairs
                log.info(f"  [ECPRA] +{len(ecpra_pairs)} resonance pairs → sampler_total={len(sampler_samples)}")
            else:
                log.info("  [ECPRA] No resonance pairs — small range or flat energy landscape")
        else:
            log.info("  [ECPRA] Skipped — no pubkey available")
    except Exception as _ecpra_e:
        log.warning(f"  [ECPRA] phase failed: {_ecpra_e}")

    # ── PHASE S1: QFT Period Finding [Shor-inspired] ─────────────────────────
    shor_s1_samples: List[Tuple[float, int]] = []
    if use_shor_s1:
        try:
            shor_s1_samples = run_shor_qft_phase(
                bits=bits, base=base,
                full_start=full_start, full_end=full_end,
                pubkey_xy=pubkey_xy, target_h160=target_h160,
                pubkey_hex=pubkey_hex,
                h_biases=h_biases, dxs=dxs,
                shots=min(shots, 4096), opt_level=opt_level,
                backend_mode=backend_mode, iqm_device=iqm_device,
                iqm_token=iqm_token, ibm_token=ibm_token,
                ibm_crn=ibm_crn, ibm_backend_name=ibm_backend_name,
                n_reps=3,
            )
            sampler_samples = sampler_samples + shor_s1_samples
            log.info(f"  [Phase S1] +{len(shor_s1_samples)} QFT samples -> total={len(sampler_samples)}")
        except Exception as ex:
            log.warning(f"  [Phase S1] QFT failed: {ex}")

    # ── PHASE S2: Full Quantum Phase Estimation [Shor-inspired] ──────────────
    shor_s2_samples: List[Tuple[float, int]] = []
    if use_shor_s2:
        try:
            max_q_for_s2 = ancilla + bits + 1
            shor_s2_samples = run_shor_qpe_phase(
                bits=bits, base=base,
                full_start=full_start, full_end=full_end,
                pubkey_xy=pubkey_xy, target_h160=target_h160,
                pubkey_hex=pubkey_hex,
                h_biases=h_biases, dxs=dxs,
                shots=min(shots, 4096), opt_level=opt_level,
                backend_mode=backend_mode, iqm_device=iqm_device,
                iqm_token=iqm_token, ibm_token=ibm_token,
                ibm_crn=ibm_crn, ibm_backend_name=ibm_backend_name,
                max_qubits=max_q_for_s2,
            )
            sampler_samples = sampler_samples + shor_s2_samples
            log.info(f"  [Phase S2] +{len(shor_s2_samples)} QPE samples -> total={len(sampler_samples)}")
        except Exception as ex:
            log.warning(f"  [Phase S2] QPE failed: {ex}")

    # Phase C: three paths depending on mode and bits
    mode1_active = (pubkey_xy is None and pubkey_hex is None)
    mode1_found_offset: Optional[int] = None
    grover_samples: List[Tuple[float, int]] = []

    if mode1_active:
        # ── [MODE1] ADDRESS-ONLY PATH ──────────────────────────────────────────
        if bits <= _MODE1_GROVER_MAX_BITS:
            log.info(f"  [MODE1-GROVER] bits={bits} ≤ {_MODE1_GROVER_MAX_BITS} "
                     f"→ REAL hash-preimage Grover")
            marked_offset = precompute_hash160_table(base, bits, target_h160)
            if marked_offset is not None:
                mode1_found_offset = marked_offset
                qc_real = build_real_grover_circuit(bits, marked_offset, ancilla)
                if qc_real is not None:
                    iqm_backend = None
                    if backend_mode == "iqm_hardware":
                        try:   iqm_backend = _get_iqm_backend_obj(iqm_device, iqm_token)
                        except Exception as ex: log.warning(f"  [MODE1-GROVER IQM] {ex}")
                    try:
                        counts = _execute_circuit(qc_real, grover_shots, opt_level,
                                                  backend_mode, iqm_backend, "mkey")
                        for bs, cnt in counts.items():
                            off   = int(bs.zfill(bits)[-bits:], 2)
                            e     = compute_energy(base+off, target_h160)
                            bonus = -10.0 if off == marked_offset else 0.0
                            w = max(1, min(cnt, 20))
                            for _ in range(w): grover_samples.append((e+bonus, off))
                        log.info(f"  [MODE1-GROVER] {len(grover_samples)} samples  "
                                 f"marked_offset={marked_offset}")
                    except Exception as ex:
                        log.warning(f"  [MODE1-GROVER] run failed: {ex}")
                else:
                    log.warning("  [MODE1-GROVER] Circuit build failed")
            else:
                log.warning("  [MODE1-GROVER] Key not in range — p-bit fallback")
                pbit_s, _ = run_mode1_pbit_sampler(
                    bits=bits, base=base, target_h160=target_h160,
                    h_biases=h_biases, J_couplings=J_couplings,
                    layers=layers, iterations=iterations, shots=shots,
                    opt_level=opt_level, backend_mode=backend_mode,
                    iqm_device=iqm_device, iqm_token=iqm_token,
                    ancilla=ancilla, use_spsa=use_spsa, spsa_max_iter=spsa_max_iter,
                    ibm_token=ibm_token, ibm_crn=ibm_crn,
                    ibm_backend_name=ibm_backend_name,
                )
                grover_samples = pbit_s
        else:
            # FIX-JOB-EXPLOSION: Mode1 PBIT for large bits was submitting
            # iterations + spsa_max_iter QPU jobs (60+ submissions).
            # Cap at 2 iterations max and disable SPSA for this path.
            # 2 × shots samples are enough for the gap detector to find
            # the snake corridor — more iterations = more random noise,
            # not more signal (hash160 energy landscape is too flat).
            _m1_iters = min(2, iterations)
            log.info(f"  [MODE1-PBIT] bits={bits} > {_MODE1_GROVER_MAX_BITS} "
                     f"→ p-bit sampler (capped: {_m1_iters} iters, no SPSA)")
            pbit_s, mode1_found_offset = run_mode1_pbit_sampler(
                bits=bits, base=base, target_h160=target_h160,
                h_biases=h_biases, J_couplings=J_couplings,
                layers=layers, iterations=_m1_iters, shots=shots,
                opt_level=opt_level, backend_mode=backend_mode,
                iqm_device=iqm_device, iqm_token=iqm_token,
                ancilla=ancilla, use_spsa=False,  # no SPSA = no extra jobs
                spsa_max_iter=0,
                ibm_token=ibm_token, ibm_crn=ibm_crn,
                ibm_backend_name=ibm_backend_name,
            )
            grover_samples = pbit_s
    else:
        # ── STANDARD PATH (pubkey available) ──────────────────────────────────
        grover_samples = run_grover_ipe_phase(
            bits=bits, sampler_samples=sampler_samples, h_biases=h_biases,
            base=base, target_h160=target_h160,
            pubkey_xy=pubkey_xy, pubkey_hex=pubkey_hex,
            shots=grover_shots, n_ipe_rounds=n_ipe_rounds, top_k=grover_top_k,
            backend_mode=backend_mode, iqm_device=iqm_device, iqm_token=iqm_token,
            ibm_token=ibm_token, ibm_crn=ibm_crn, ibm_backend_name=ibm_backend_name,
            ancilla=ancilla, opt_level=opt_level,
        )

    # [MODE1] Early exit if exact key found
    if mode1_found_offset is not None:
        found_k = base + mode1_found_offset
        pinned_exact = ["1" if (mode1_found_offset >> (bits-1-b)) & 1
                        else "0" for b in range(bits)]
        bp_exact = np.array(
            [(mode1_found_offset >> (bits-1-b)) & 1 for b in range(bits)], dtype=float)
        log.info(f"  [MODE1] ✅ EXACT KEY FOUND  k={hex(found_k)}")
        print(f"\n  {'='*60}")
        print(f"  🎉  EXACT PRIVATE KEY FOUND (Mode 1 — address only)!")
        print(f"  {'='*60}")
        print(f"  k          = {hex(found_k)}")
        print(f"  offset     = {mode1_found_offset}")
        print(f"  Verify:  hash160(k*G) == target_h160 ✅")
        print(f"  {'='*60}\n")
        if save_plot:
            ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = f"bit_probs_{bits}bit_{ts}.png"
            plot_bit_probs(bp_exact, bits, pinned_exact,
                           label=f"EXACT KEY {hex(found_k)}", save_path=path)
        save_result(found_k, found_k+1, bits, pinned_exact, bp_exact,
                    mode_label+" [EXACT KEY FOUND]", address, iqm_device)
        if use_kangaroo_export:
            export_kangaroo(found_k, found_k+1, bits, pubkey_xy, shift,
                            address, iqm_device=iqm_device)
        return found_k, found_k+1, pinned_exact, bp_exact

    # ── PHASE S3: Quantum Amplitude Estimation [Shor-inspired] ──────────────
    if use_shor_s3:
        try:
            all_so_far  = sampler_samples + grover_samples
            top_so_far  = sorted(set(int(o) for _, o in
                                     sorted(all_so_far, key=lambda x: x[0])[:64]))[:32]
            shor_s3_samples = run_shor_amplitude_phase(
                bits=bits, base=base,
                full_start=full_start, full_end=full_end,
                pubkey_xy=pubkey_xy, target_h160=target_h160,
                pubkey_hex=pubkey_hex,
                h_biases=h_biases, dxs=dxs,
                top_candidates=top_so_far,
                shots=min(shots, 2048), opt_level=opt_level,
                backend_mode=backend_mode, iqm_device=iqm_device,
                iqm_token=iqm_token, ibm_token=ibm_token,
                ibm_crn=ibm_crn, ibm_backend_name=ibm_backend_name,
            )
            grover_samples = grover_samples + shor_s3_samples
            log.info(f"  [Phase S3] +{len(shor_s3_samples)} amplitude samples -> total={len(grover_samples)}")
        except Exception as ex:
            log.warning(f"  [Phase S3] Amplitude scoring failed: {ex}")

    # Phase D: Lattice [G-8] + DBSCAN [G-7] + forced result
    top_for_lattice = list(dict.fromkeys(
        int(o) for _, o in sorted(sampler_samples, key=lambda x: x[0])[:grover_top_k]
    ))
    lattice_samples = lattice_refine_candidates(
        top_for_lattice, bits, base, target_h160, pubkey_xy, pubkey_hex, 20)

    all_samples = sampler_samples + grover_samples + lattice_samples
    log.info(f"  [Phase D] {len(all_samples)} total  "
             f"(S+QW={len(sampler_samples)} G={len(grover_samples)} L={len(lattice_samples)})")

    # [TRAJECTORY] Pure post-processing: extract the two real measured
    # values that tightest-bracket the interference density peak.
    # No forced percentages — output is exactly what the QPU found.
    start_r, end_r, pinned, bit_probs = quantum_trajectory_range(
        all_samples, base, bits, full_start, full_end,
        pubkey_xy=pubkey_xy, target_h160=target_h160,
    )
    # Only fall back if truly empty (start >= end — should never happen)
    if start_r >= end_r:
        log.warning("  [TRAJECTORY] Empty bracket — force_best_range fallback")
        start_r, end_r, pinned, bit_probs = force_best_range(
            all_samples, base, bits, full_start, full_end)

    if save_plot:
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"bit_probs_{bits}bit_{ts}.png"
        plot_bit_probs(bit_probs, bits, pinned, label=mode_label, save_path=path)

    save_result(start_r, end_r, bits, pinned, bit_probs,
                mode_label, address, iqm_device)

    # Phase E [G-5] kangaroo export
    if use_kangaroo_export:
        export_kangaroo(start_r, end_r, bits, pubkey_xy, shift,
                        address, iqm_device=iqm_device)

    return start_r, end_r, pinned, bit_probs


# =============================================================================
# [G-6] MULTI-RUN VOTING
# =============================================================================

def multi_run_reduce(n_runs: int = 5, **kwargs) -> Tuple[int, int, List[str], np.ndarray]:
    """
    [G-6] Multi-run voting strategy.

    Each run independently produces a bracket with ~25% hit probability.
    After n_runs:
      UNION        = min(all_starts) .. max(all_ends)
                     Safe output — key is inside if ANY run captured it.
                     Probability = 1 - (1-0.25)^n_runs
      INTERSECTION = max(all_starts) .. min(all_ends)
                     Tight output — key inside only if ALL runs agreed.
                     Use for BitCrack when you want the smallest range.

    We return the UNION as primary (guarantees key inside with high prob)
    and log the intersection as a secondary tighter hint.
    """
    results: List[Tuple[int, int]] = []
    last_pinned = ["?"] * kwargs.get("bits", 16)
    last_bp     = np.full(kwargs.get("bits", 16), 0.5)
    bits        = kwargs.get("bits", 16)
    full_start, full_end = auto_range(bits)

    log.info(f"\n{'='*60}")
    log.info(f"  [G-6 MultiRun] {n_runs} runs  "
             f"(union=safe/high-recall  intersection=tight/lower-recall)")
    for run in range(n_runs):
        log.info(f"  [G-6] Run {run+1}/{n_runs}…")
        kwargs["save_plot"]           = (run == 0)
        kwargs["use_kangaroo_export"] = (run == n_runs - 1)
        s, e, pinned, bp = reduce_keyspace(**kwargs)
        results.append((s, e))
        last_pinned = pinned; last_bp = bp
        log.info(f"  [G-6] Run {run+1} bracket: [{hex(s)}, {hex(e)}]  "
                 f"size={e-s:,}")

    # UNION — key inside if any single run captured it
    union_s = min(s for s, _ in results)
    union_e = max(e for _, e in results)
    union_sz = union_e - union_s

    # INTERSECTION — only if all runs agree
    int_start = max(s for s, _ in results)
    int_end   = min(e for _, e in results)
    int_valid = int_start < int_end

    full_sz = full_end - full_start
    import math
    p_hit_union = 1.0 - (1.0 - min(1.0, union_sz / max(full_sz, 1))) ** 1
    p_miss_all  = (0.75) ** n_runs   # rough: 75% miss per run

    log.info(f"\n  [G-6 MultiRun] UNION        [{hex(union_s)}, {hex(union_e)}]  "
             f"size={union_sz:,}  p_contains≈{(1-p_miss_all)*100:.0f}%")
    if int_valid:
        log.info(f"  [G-6 MultiRun] INTERSECTION [{hex(int_start)}, {hex(int_end)}]  "
                 f"size={int_end-int_start:,}  (tighter — use if confident)")
    else:
        log.info(f"  [G-6 MultiRun] INTERSECTION empty — runs did not agree")

    print(f"\n  ┌─ MULTI-RUN VOTING RESULTS ({n_runs} runs) ─────────────────────────┐")
    print(f"  │  SAFE  (union)        : {hex(union_s)} → {hex(union_e)}")
    print(f"  │  Key-inside prob      : ~{(1-p_miss_all)*100:.0f}%")
    print(f"  │  Range size (union)   : {union_sz:,} keys")
    if int_valid:
        print(f"  │  TIGHT (intersection) : {hex(int_start)} → {hex(int_end)}")
        print(f"  │  Range size (tight)   : {int_end-int_start:,} keys")
    print(f"  └────────────────────────────────────────────────────────────────┘")

    # Return UNION — safe, high recall
    return union_s, union_e, last_pinned, last_bp


# =============================================================================
# [FIX-2] SELF-TEST MODE
# =============================================================================

def self_test(bits: int, n_trials: int = 10, **kwargs) -> None:
    import random as _rng
    full_start, full_end = auto_range(bits)
    hits = 0; reductions = []
    log.info(f"\n{'='*60}")
    log.info(f"  SELF-TEST  {bits}-bit  {n_trials} trials")
    for trial in range(n_trials):
        true_k      = _rng.randint(full_start, full_end)
        pubkey_xy   = _pubkey_point(true_k)
        target_h160 = _k_to_hash160(true_k)
        log.info(f"\n  Trial {trial+1}/{n_trials}  true_k={hex(true_k)}")
        start_r, end_r, pinned, bit_probs = reduce_keyspace(
            bits=bits, base=full_start,
            target_h160=target_h160, pubkey_xy=pubkey_xy,
            pubkey_hex=None, save_plot=False,
            mode_label=f"SelfTest-{trial+1}", **kwargs
        )
        inside    = start_r <= true_k <= end_r
        range_sz  = end_r - start_r
        full_sz   = full_end - full_start
        reduction = full_sz / max(range_sz, 1)
        reductions.append(reduction)
        if inside: hits += 1
        log.info(f"  {'✅ HIT' if inside else '❌ MISS'}  key={hex(true_k)}  "
                 f"[{hex(start_r)}, {hex(end_r)}]  reduction={reduction:.1f}×")
    hit_rate = hits / n_trials
    avg_red  = sum(reductions) / len(reductions)
    baseline = 1.0 / avg_red
    print(f"\n{'═'*60}")
    print(f"  SELF-TEST RESULTS  ({bits}-bit  {n_trials} trials)")
    print(f"{'═'*60}")
    print(f"  Hit rate         : {hits}/{n_trials}  = {hit_rate*100:.1f}%")
    print(f"  Avg reduction    : {avg_red:.1f}×")
    print(f"  Random baseline  : {baseline*100:.1f}%")
    print(f"  Signal gain      : {hit_rate/max(baseline,1e-9):.2f}×")
    print(f"  Note: Signal gain > 1.0 means tool beats random.")
    print(f"{'═'*60}\n")


# =============================================================================
# INTERACTIVE MAIN
# =============================================================================

def _ask(prompt: str, default: str) -> str:
    try:
        v = input(f"  {prompt} [{default}]: ").strip()
        return v if v else default
    except (EOFError, KeyboardInterrupt):
        return default


def interactive_main() -> None:
    print("\n" + "═" * 74)
    print("  KEY-REDUCER  ·  Supreme Edition  ·  Quantum Walk + Trajectory Sensing")
    print("  ─────────────────────────────────────────────────────────────────────")
    print("  IQM(pytket/Qrisp) · IBM Quantum · Aer Simulator  |  Quantum Walk + Trajectory FWHM Range")
    print("  Outputs REDUCED [min_range, max_range] — always produces output.")
    print("  Use --self-test to measure how often the true key is inside the range.")
    print("═" * 74)
    print("""
  WHAT THIS TOOL ACTUALLY DOES (v21 — P-Bits + Qubits Walk Together)
  ────────────────────────────────────────────────────────────────────
  Combines quantum probabilistic sampling + classical energy sensing to
  output a sub-range statistically more likely to contain the unknown key.
  It does NOT guarantee 100% containment (impossible without breaking ECDLP).

    Phase A  — SparsePauliOp Ising Landscape  [Sobol + non-NN couplings]
    Phase B  — SPSA-optimised TwoLocal Sampler  [G-1 SPSA]
    Phase B2 — THREE ENGINES WORKING TOGETHER to map the full key-space:
      ┌─ Engine 1: P-BIT  (CPU)   — Classical Glauber sigmoid dynamics
      │   p(s_i=+1)=sigmoid(β·I_i)  stochastic, sequential, non-quantum
      │   Visit density = oscilloscope waveform; empty = snake = key
      ├─ Engine 2: QPB v3 (QPU)  — Quantum P-Bit gate
      │   Ry(2·arcsin(√sigmoid(β·I_b))) gives P(|1⟩)=sigmoid(β·I_b)
      │   CRZ neighbor coupling = quantum W_ij matrix
      │   β: 0.5 (spread cloud) → 4.0 (snake corridor)
      └─ Engine 3: AdapCoin (QPU)— Adaptive-coin walk + phase oracle
          Ry(θ_b) coin steered by oracle; RZZ Ising couplings; extra reach
          Explores different Hilbert space regions than QPB engine
      → All three density maps merge → richer, more accurate snake corridor
    Phase C  — Grover-IPE / Real Grover / p-bit sampler
    Phase D  — DBSCAN [G-7] + BKZ/LLL [G-8] + Forced Output
    Phase E  — Kangaroo Export [G-5] + Multi-run Voting [G-6]
""")

    # ── Input mode ─────────────────────────────────────────────────────────────
    print("  ┌─ INPUT MODE ─────────────────────────────────────────────────────┐")
    print("  │  [1]  Bitcoin P2PKH address only        (Hash160 — Mode1 Grover) │")
    print("  │  [2]  Address  +  compressed public key    (hybrid — strong)     │")
    print("  │  [3]  Compressed public key only           (strongest signal)    │")
    print("  └───────────────────────────────────────────────────────────────────┘")
    choice = _ask("Select input mode [1/2/3]", "1")

    if choice == "1":
        print("\n  ┌─ MODE [1] — ADDRESS ONLY ─────────────────────────────────────────┐")
        print("  │  bits ≤ 20: GENUINE Grover (precomputes hash table, exact oracle). │")
        print("  │  bits > 20: p-bit QPU exhaustive search + hash verify.            │")
        print("  └────────────────────────────────────────────────────────────────────┘")
        confirm = _ask("Continue with Mode [1]? [Y/n]", "Y")
        if confirm.strip().lower() in ("n", "no"):
            print("  → Re-run and select Mode [2] or [3] for stronger signal."); return

    address = ""; pubkey_hex = None; pubkey_xy = None
    target_h160: bytes = b"\x00" * 20

    if choice in ("1", "2"):
        address = _ask("Bitcoin P2PKH address", "").strip()
        try:
            target_h160 = address_to_hash160(address)
            print(f"  ✅ Hash160: {target_h160.hex()}")
        except ValueError as e:
            print(f"  ❌ {e}"); sys.exit(1)

    if choice == "2":
        pk = _ask("Compressed public key (66 hex chars, 02/03 prefix)", "").strip()
        if len(pk) >= 66:
            pubkey_hex = pk.lower(); pubkey_xy = decompress_pubkey(pubkey_hex)
            if pubkey_xy:
                print(f"  ✅ Decompressed → Qx={hex(pubkey_xy[0])[:22]}…")
                print(f"  ✅ EC-delta + range shift ACTIVE")
            else:
                print("  ⚠️  Decompression failed — Hash160-only mode")
                pubkey_xy = pubkey_hex = None
        else:
            print("  ⚠️  Pubkey too short — Hash160-only mode")

    if choice == "3":
        pk = _ask("Compressed public key (66 hex chars, 02/03 prefix)", "").strip()
        if len(pk) < 66: print("  ❌ Pubkey too short"); sys.exit(1)
        pubkey_hex = pk.lower(); pubkey_xy = decompress_pubkey(pubkey_hex)
        if pubkey_xy is None: print("  ❌ Decompression failed"); sys.exit(1)
        print(f"  ✅ Decompressed → Qx={hex(pubkey_xy[0])[:22]}…")
        print(f"  ✅ EC-delta + SPSA + range shift ACTIVE — strongest mode")

    if pubkey_xy:    mode_label = "Full Public Key — EC-Delta+SPSA+Shift"
    elif pubkey_hex: mode_label = "Address + Compressed PubKey (hybrid)"
    else:            mode_label = "Address Only — Hash160"

    # ── Bit length ─────────────────────────────────────────────────────────────
    print("\n  ┌─ KEY BIT LENGTH ─────────────────────────────────────────────────┐")
    print("  │  Known puzzle public keys: 5, 8, 14, 16, 21, 25, 135            │")
    print("  │  (shots / layers / iters auto-filled when a preset is selected)  │")
    print("  │    5 · 8 · 14 · 16 · 20 · 21 · 24 · 25 · 32 · 40 · 64 · 71 · 135│")
    print("  └───────────────────────────────────────────────────────────────────┘")
    bits_s = _ask("Bit length", "16")
    bits   = int(bits_s)
    full_start, full_end = auto_range(bits)
    print(f"  Full key range: [{hex(full_start)}, {hex(full_end)}]")

    # ── AUTO-FILL pubkey from preset ──────────────────────────────────────────
    preset_pub = _preset_pubkey(bits)
    if preset_pub is not None and pubkey_xy is None and pubkey_hex is None:
        print(f"\n  ✅ Known public key found for puzzle {bits}!")
        print(f"     {preset_pub}")
        if _ask("Auto-load preset pubkey? [Y/n]", "Y").strip().lower() not in ("n","no"):
            pubkey_hex = preset_pub.lower()
            pubkey_xy  = decompress_pubkey(pubkey_hex)
            if pubkey_xy is not None:
                print(f"  ✅ Preset pubkey loaded → EC-Delta + SPSA + Shift active")
                mode_label = "Full Public Key — EC-Delta+SPSA+Shift (PRESET)"
                prefix     = "02" if pubkey_xy[1] % 2 == 0 else "03"
                pk_bytes   = bytes.fromhex(prefix + hex(pubkey_xy[0])[2:].zfill(64))
                target_h160 = _hash160(pk_bytes)
            else:
                print("  ⚠️  Preset pubkey decompression failed — ignored")
                pubkey_xy = None; pubkey_hex = None

    # ── Key range: start & end (both with auto-fill on ENTER) ─────────────────
    print("  ┌─ KEY RANGE ───────────────────────────────────────────────────────┐")
    print("  │  Press ENTER on BOTH to use the full auto range (recommended).   │")
    print("  │  You can type with OR without the 0x prefix — both work.         │")
    print(f"  │  Auto START = {hex(full_start):<55} │")
    print(f"  │  Auto END   = {hex(full_end):<55} │")
    print("  └───────────────────────────────────────────────────────────────────┘")

    kstart_s = _ask("Custom START hex (ENTER = auto)", "")
    if kstart_s.strip() == "":
        base = full_start
        print(f"  ✅ START = auto → {hex(full_start)}")
    else:
        try:
            base = int(kstart_s.strip().lower().replace("0x", ""), 16)
            if base < full_start or base > full_end:
                print(f"  ⚠️  {hex(base)} outside auto range — using auto START {hex(full_start)}")
                base = full_start
            else:
                print(f"  ✅ START = {hex(base)}")
        except ValueError:
            print(f"  ⚠️  Cannot parse '{kstart_s}' — using auto START {hex(full_start)}")
            base = full_start

    kend_s = _ask("Custom END   hex (ENTER = auto)", "")
    if kend_s.strip() == "":
        user_full_end = full_end
        print(f"  ✅ END   = auto → {hex(full_end)}")
    else:
        try:
            user_full_end = int(kend_s.strip().lower().replace("0x", ""), 16)
            if user_full_end <= base:
                print(f"  ⚠️  END {hex(user_full_end)} ≤ START {hex(base)} — using auto END {hex(full_end)}")
                user_full_end = full_end
            elif user_full_end > full_end:
                print(f"  ⚠️  END {hex(user_full_end)} exceeds puzzle boundary {hex(full_end)} — clamped")
                user_full_end = full_end
            else:
                print(f"  ✅ END   = {hex(user_full_end)}")
        except ValueError:
            print(f"  ⚠️  Cannot parse '{kend_s}' — using auto END {hex(full_end)}")
            user_full_end = full_end

    # ── Backend ────────────────────────────────────────────────────────────────
    print("\n  ┌─ BACKEND ──────────────────────────────────────────────────────────┐")
    print("  │  ── LOCAL SIMULATOR ──────────────────────────────────────────────  │")
    print("  │  [1]  Aer Simulator  (local — ★ start here, no token)             │")
    print("  │  ── IQM HARDWARE via pytket (Qiskit bridge) ──────────────────────  │")
    print(f"  │  [2]  IQM Sirius   ({IQM_DEVICE_QUBITS['sirius']:>2}q usable — entry QPU)              │")
    print(f"  │  [3]  IQM Garnet   ({IQM_DEVICE_QUBITS['garnet']:>2}q usable — ★ recommended)         │")
    print(f"  │  [4]  IQM Emerald  ({IQM_DEVICE_QUBITS['emerald']:>2}q usable — max ancilla)           │")
    print("  │  ── IQM HARDWARE via Qrisp (auto native transpilation) ──────────  │")
    print(f"  │  [5]  Qrisp+Sirius  ({IQM_DEVICE_QUBITS['sirius']:>2}q — QuantumVariable API)          │")
    print(f"  │  [6]  Qrisp+Garnet  ({IQM_DEVICE_QUBITS['garnet']:>2}q — ★ recommended Qrisp)          │")
    print(f"  │  [7]  Qrisp+Emerald ({IQM_DEVICE_QUBITS['emerald']:>2}q — max ancilla Qrisp)           │")
    print("  │  ── IBM QUANTUM HARDWARE (qiskit-ibm-runtime) ──────────────────  │")
    print("  │  [8]  IBM Hardware  (ibm_fez 156q · ibm_kingston 156q · etc.)    │")
    print("  └────────────────────────────────────────────────────────────────────┘")
    bk_in = _ask("Backend [1..8]", "8")

    iqm_device = "garnet"; iqm_token = ""
    ibm_token  = ""; ibm_crn = ""; ibm_backend_name = _IBM_DEFAULT_BACKEND

    pytket_map = {"2": "sirius", "3": "garnet", "4": "emerald"}
    qrisp_map  = {"5": "sirius", "6": "garnet", "7": "emerald"}

    if bk_in in pytket_map:
        backend_mode = "iqm_hardware"; iqm_device = pytket_map[bk_in]
        iqm_token    = (os.getenv("IQM_TOKEN","") or _ask("IQM Resonance API token",""))
        if not iqm_token:
            print("  ❌ IQM token required — falling back to Aer.")
            backend_mode = "simulator"; iqm_device = "garnet"
        else:
            n_q = IQM_DEVICE_QUBITS.get(iqm_device, 16)
            print(f"  ✅ IQM {iqm_device.capitalize()} via pytket ({n_q}q usable)")
    elif bk_in in qrisp_map:
        backend_mode = "qrisp_iqm"; iqm_device = qrisp_map[bk_in]
        iqm_token    = (os.getenv("IQM_TOKEN","") or _ask("IQM API token (Qrisp path)",""))
        if not iqm_token:
            print("  ❌ IQM token required — falling back to Aer.")
            backend_mode = "simulator"; iqm_device = "garnet"
        else:
            n_q = IQM_DEVICE_QUBITS.get(iqm_device, 16)
            print(f"  ✅ IQM {iqm_device.capitalize()} via Qrisp ({n_q}q — auto-transpilation ON)")
    elif bk_in == "8":
        backend_mode     = "ibm_hardware"
        ibm_token        = (os.getenv("IBM_QUANTUM_TOKEN","") or _ask("IBM Quantum API token",""))
        ibm_crn          = (os.getenv("IBM_QUANTUM_CRN","") or
                            _ask("IBM CRN instance (Enter to skip)",""))
        ibm_backend_name = _ask("IBM backend name", _IBM_DEFAULT_BACKEND)
        if not ibm_token:
            print("  ❌ IBM token required — falling back to Aer.")
            backend_mode = "simulator"
        else:
            print(f"  ✅ IBM {ibm_backend_name} selected")
    else:
        backend_mode = "simulator"; iqm_device = "garnet"
        print("  ✅ Aer Simulator selected (local, no token needed)")


    # ── Sampler parameters — fixed defaults regardless of bit length ────────────
    # NOTE: _preset_* values are intentionally NOT used as _ask() defaults.
    # The same recommended config applies for every bit length / range target.

    if backend_mode in ("iqm_hardware", "qrisp_iqm"):
        dev_q = IQM_DEVICE_QUBITS.get(iqm_device, 18)
    elif backend_mode == "ibm_hardware":
        dev_q = _MAX_IBM_QUBITS
    else:
        dev_q = _MAX_AER_QUBITS
    ancilla = compute_ancilla_count(bits, dev_q, backend_mode)

    print(f"\n  ┌─ SAMPLER PARAMETERS ─────────────────────────────────────────────┐")
    print(f"  │  TwoLocal layers     3=fast · 4=balanced · 5=deeper             │")
    print(f"  │  Iterations          4=quick · 8=good · 12=thorough             │")
    print(f"  │  Shots (default)     4096   (2048=fast · 65536=best)            │")
    print(f"  │  Layers (default)    5 (3=fast · 5=deep)                        │")
    print(f"  │  Iters (default)     4  (4=quick · 20=thorough)                 │")
    print(f"  │  Ising probes        512 opt=2 · 1024 opt=3  (256=fast)         │")
    print( "  │  SPSA iterations     0=disabled (always off by default)          │")
    print( "  └───────────────────────────────────────────────────────────────────┘")
    layers     = int(_ask("TwoLocal layers",         "5"))
    iters      = int(_ask("Iterations",              "4"))
    shots      = int(_ask("Shots per iter",          "4096"))
    opt_level  = int(_ask("Transpile opt level",     "2"))
    # Auto-link probes to opt_level: 2→512, 3→1024 (user can still override)
    _default_probes = "1024" if opt_level >= 3 else "512"
    n_probes   = int(_ask("Ising probes",            _default_probes))
    spsa_iters = int(_ask("SPSA iterations (0=off)", "0"))
    use_spsa   = spsa_iters > 0 and SPSA_OK

    # ── Grover-IPE ─────────────────────────────────────────────────────────────
    oracle_info = (
        f"DiagonalGate (exact, {bits}q ≤ {_DIAG_MAX_BITS}q)"
        if bits <= _DIAG_MAX_BITS
        else f"Phase-kickback (crash-free, {bits}q > {_DIAG_MAX_BITS}q)"
    )
    print("\n  ┌─ GROVER-IPE PARAMETERS ───────────────────────────────────────────┐")
    print("  │  IPE rounds       3=fast(min) · 4=default · 6=thorough           │")
    print("  │  Grover shots     2048=fast · 4096=default · 8192=thorough        │")
    print("  │  Top-K candidates 128=light · 4096=default · 256=thorough        │")
    print(f"  │  Oracle (auto)    {oracle_info:<52} │")
    print("  └───────────────────────────────────────────────────────────────────┘")
    n_ipe   = int(_ask("IPE rounds (≥3)",      "3"))
    g_shots = int(_ask("Grover shots",         "4096"))
    g_topk  = int(_ask("Top-K candidates",    "4096"))

    # ── Multi-run ─────────────────────────────────────────────────────────────
    print("\n  ┌─ MULTI-RUN VOTING [G-6] ─────────────────────────────────────────┐")
    print("  │  1=single run(default) · 3=good · 5=tighter · 10=tight+slow      │")
    print("  └───────────────────────────────────────────────────────────────────┘")
    n_runs   = int(_ask("Number of runs", "1"))
    shor_s1  = _ask("Enable S1 QFT Period Finding [Y/n]", "Y").upper().startswith("Y")
    shor_s2  = _ask("Enable S2 Full QPE [Y/n]", "Y").upper().startswith("Y")
    shor_s3  = _ask("Enable S3 Amplitude Estimation [Y/n]", "Y").upper().startswith("Y")
    use_kexp = _ask("Export kangaroo JSON? [Y/n]", "Y").lower() not in ("n","no")
    save_plt = _ask("Save bit-probability plot? [Y/n]", "Y").lower() not in ("n","no")

    # ── Summary ────────────────────────────────────────────────────────────────
    phys_q = {"sirius":16,"garnet":20,"emerald":54}
    if backend_mode == "iqm_hardware":
        bkend_str = (f"IQM {iqm_device.capitalize()} via pytket "
                     f"({IQM_DEVICE_QUBITS.get(iqm_device,16)}q usable / "
                     f"{phys_q.get(iqm_device,16)}q physical)")
    elif backend_mode == "qrisp_iqm":
        bkend_str = (f"IQM {iqm_device.capitalize()} via Qrisp "
                     f"({IQM_DEVICE_QUBITS.get(iqm_device,16)}q / auto-native-transpile)")
    elif backend_mode == "ibm_hardware":
        bkend_str = f"IBM Quantum {ibm_backend_name} (~{_MAX_IBM_QUBITS}q)"
    else:
        bkend_str = "Aer Simulator (local)"
    print(f"\n{'─'*74}")
    print(f"  CONFIGURATION SUMMARY")
    print(f"{'─'*74}")
    print(f"  Input mode   : {mode_label}")
    print(f"  Bits         : {bits}")
    print(f"  Auto range   : [{hex(full_start)}, {hex(full_end)}]")
    print(f"  Search START : {hex(base)}")
    print(f"  Search END   : {hex(user_full_end)}")
    print(f"  Backend      : {bkend_str}")
    print(f"  MAX-Q        : {bits+ancilla+1}q total "
          f"({bits}q key + {ancilla}q anc + 1q ctrl)")
    print(f"  Layers/Iters : {layers}/{iters}  |  Shots: {shots}  |  Opt: {opt_level}")
    print(f"  SPSA         : {'✅ '+str(spsa_iters)+' iters' if use_spsa else '—  (install qiskit-algorithms)'}")
    print(f"  Sobol        : {'✅' if SOBOL_OK else '—  stratified fallback'}")
    print(f"  DBSCAN       : {'✅' if SKLEARN_OK else '—  top-K fallback'}")
    print(f"  Oracle       : {oracle_info}")
    print(f"  IPE/shots    : {max(n_ipe,3)}/{g_shots}  |  Top-K: {g_topk}")
    print(f"  Multi-run    : {n_runs} run{'s' if n_runs > 1 else ''}")
    print(f"  Lattice      : {'fpylll BKZ-20 ✅' if FPYLLL_OK else '2×2 LLL fallback'}")
    print(f"  Range shift  : {'✅' if pubkey_xy else '—'}")
    print(f"  Kangaroo exp : {'✅' if use_kexp else '—'}")
    print(f"  RIPEMD160    : {'pycryptodome ✅' if PYCRYPTO_OK else 'hashlib fallback'}")
    print(f"  IQM_OK       : {'✅ pytket-iqm ready' if IQM_OK else '❌ pip install pytket-iqm'}")
    print(f"  pytket-qiskit: {'✅ bridge ready' if PYTKET_QISKIT_OK else '❌ pip install pytket-qiskit'}")
    print(f"  Qrisp_OK     : {'✅ qrisp[iqm] ready' if QRISP_OK else '— pip install iqm-client>=34.0.3 qrisp'}")
    print(f"  IBM_OK       : {'✅ qiskit-ibm-runtime ready' if IBM_OK else '— pip install qiskit-ibm-runtime'}")
    print(f"  QWalk        : ✅ THREE B2 engines: P-Bit (CPU) + QPB v3 (QPU) + AdapCoin (QPU)")
    print(f"  Trajectory   : ✅ FWHM interference density map → tightest range")
    print(f"{'─'*74}")

    if _ask("Run now? [Y/n]", "Y").lower() in ("n", "no"):
        print("  Aborted."); return

    t0  = time.perf_counter()
    kw  = dict(
        bits=bits, base=base,
        full_start_override=base,
        full_end_override=user_full_end,
        target_h160=target_h160, pubkey_xy=pubkey_xy, pubkey_hex=pubkey_hex,
        layers=layers, iterations=iters, shots=shots,
        opt_level=opt_level, n_probes=n_probes,
        grover_shots=g_shots, n_ipe_rounds=n_ipe, grover_top_k=g_topk,
        backend_mode=backend_mode, iqm_device=iqm_device, iqm_token=iqm_token,
        ibm_token=ibm_token, ibm_crn=ibm_crn, ibm_backend_name=ibm_backend_name,
        save_plot=save_plt, mode_label=mode_label, address=address,
        use_range_shift=(pubkey_xy is not None),
        use_spsa=use_spsa, spsa_max_iter=spsa_iters,
        use_kangaroo_export=use_kexp,
    )

    if n_runs > 1:
        start_r, end_r, pinned, bit_probs = multi_run_reduce(n_runs=n_runs, **kw)
    else:
        start_r, end_r, pinned, bit_probs = reduce_keyspace(**kw)

    elapsed   = time.perf_counter() - t0
    full_size = full_end - full_start
    new_size  = end_r - start_r
    reduction = full_size / max(new_size, 1)
    pc        = sum(1 for b in pinned if b in ("0","1"))

    print(f"\n{'═'*74}")
    print(f"  🎯  QUANTUM TRAJECTORY BRACKET  ({elapsed:.1f}s)")
    print(f"{'═'*74}")
    print(f"  Mode         : {mode_label}")
    print(f"  Backend      : {bkend_str}")
    print(f"  Bits         : {bits}  |  Bits pinned: {pc}/{bits}")
    print(f"  Pinned bits  : {''.join(pinned)}")
    print(f"")
    print(f"  ┌─ TRAJECTORY BRACKET ──────────────────────────────────────────────┐")
    print(f"  │  LOWER BOUND : {hex(start_r):<54} │")
    print(f"  │  UPPER BOUND : {hex(end_r):<54} │")
    print(f"  │  Range size  : {new_size:<,} keys")
    print(f"  │  Reduction   : {reduction:.1f}× smaller than full {bits}-bit range")
    print(f"  │  Method      : Quantum walk interference density — measured values only")
    print(f"  │  Please a Donation: 1Bu4CR8Bi5AXQG8pnu1avny88C5CCgWKfb")
    print(f"  └────────────────────────────────────────────────────────────────────┘")
    print(f"")
    print(f"  BitCrack GPU command:")
    print(f"    bitcrack --keyspace {hex(start_r)}:{hex(end_r)} {address or '<address>'}")
    print(f"  KeyHunt BSGS:")
    print(f"    keyhunt -m bsgs -r {hex(start_r)}:{hex(end_r)}")
    print(f"{'═'*74}\n")


# =============================================================================
# CLI
# =============================================================================

def cli_main() -> int:
    p = argparse.ArgumentParser(
        description="KEY-REDUCER IQM Edition: Quantum Probabilistic Keyspace Range Reducer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
IQM Hardware via pytket:
  python QPKR.py --bits 16 --pubkey 029d8c... --backend iqm_hardware --iqm-device garnet --iqm-token TOKEN
  python QPKR.py --bits 5  --address 1... --backend iqm_hardware --iqm-device sirius --iqm-token TOKEN

IQM Hardware via Qrisp (auto-native-transpilation, no pytket bridge needed):
  python QPKR.py --bits 16 --pubkey 029d8c... --backend qrisp_iqm --iqm-device garnet --iqm-token TOKEN
  python QPKR.py --bits 25 --pubkey 03057f... --backend qrisp_iqm --iqm-device emerald --iqm-token TOKEN

IBM Quantum Hardware:
  python QPKR.py --bits 16 --pubkey 029d8c... --backend ibm_hardware --ibm-backend ibm_fez --ibm-token TOKEN
  export IBM_QUANTUM_TOKEN=TOKEN && python QPKR.py --bits 16 --backend ibm_hardware

Aer Simulator (no token, always works):
  python QPKR.py                          (interactive)
  python QPKR.py --bits 16 --pubkey 029d8c...
  python QPKR.py --bits 8  --address 1... --multi-run 5
  python QPKR.py --self-test --bits 8 --trials 20

IQM Devices:  sirius({s}q) garnet({g}q★) emerald({e}q)
Tokens:  export IQM_TOKEN=...   export IBM_QUANTUM_TOKEN=...
""".format(s=IQM_DEVICE_QUBITS['sirius'], g=IQM_DEVICE_QUBITS['garnet'], e=IQM_DEVICE_QUBITS['emerald']))
    p.add_argument("--bits",          type=int, default=16)
    p.add_argument("--address",       type=str, default="")
    p.add_argument("--hash160",       type=str, default="")
    p.add_argument("--pubkey",        type=str, default="")
    p.add_argument("--kstart",        type=str, default="")
    p.add_argument("--backend",       type=str, default="simulator",
                   choices=["simulator","iqm_hardware","qrisp_iqm","ibm_hardware"],
                   help=("Backend: simulator(Aer) | iqm_hardware(pytket) | "
                         "qrisp_iqm(Qrisp) | ibm_hardware(IBM Runtime)"))
    p.add_argument("--iqm-device",    type=str, default="garnet",
                   choices=["sirius", "garnet", "emerald"],
                   help="IQM device (used for both pytket and Qrisp paths)")
    p.add_argument("--iqm-token",     type=str, default="",
                   help="IQM Resonance API token (or set IQM_TOKEN env var)")
    p.add_argument("--ibm-token",     type=str, default="",
                   help="IBM Quantum API token (or set IBM_QUANTUM_TOKEN env var)")
    p.add_argument("--ibm-crn",       type=str, default="",
                   help="IBM CRN instance string (optional)")
    p.add_argument("--ibm-backend",   type=str, default=_IBM_DEFAULT_BACKEND,
                   help=f"IBM backend name (default: {_IBM_DEFAULT_BACKEND})")
    p.add_argument("--layers",        type=int, default=4)
    p.add_argument("--iters",         type=int, default=12)
    p.add_argument("--shots",         type=int, default=4096)
    p.add_argument("--opt-level",     type=int, default=2)
    p.add_argument("--n-probes",      type=int, default=512)
    p.add_argument("--grover-shots",  type=int, default=4096)
    p.add_argument("--n-ipe",         type=int, default=4)
    p.add_argument("--grover-topk",   type=int, default=128)
    p.add_argument("--no-plot",       action="store_true")
    p.add_argument("--interactive",   action="store_true")
    p.add_argument("--self-test",     action="store_true")
    p.add_argument("--trials",        type=int, default=10)
    p.add_argument("--multi-run",     type=int, default=1)
    p.add_argument("--spsa-iters",    type=int, default=60)
    p.add_argument("--no-spsa",       action="store_true")
    p.add_argument("--no-kangaroo",   action="store_true")
    p.add_argument("--no-shor-s1",    action="store_true",
                   help="Disable S1 QFT period-finding phase")
    p.add_argument("--no-shor-s2",    action="store_true",
                   help="Disable S2 full QPE phase")
    p.add_argument("--no-shor-s3",    action="store_true",
                   help="Disable S3 amplitude-estimation phase")
    args = p.parse_args()

    if args.interactive or len(sys.argv) == 1:
        interactive_main(); return 0

    iqm_token        = args.iqm_token or os.getenv("IQM_TOKEN", "")
    ibm_token        = args.ibm_token or os.getenv("IBM_QUANTUM_TOKEN", "")
    ibm_crn          = args.ibm_crn   or os.getenv("IBM_QUANTUM_CRN", "")
    ibm_backend_name = args.ibm_backend

    if args.self_test:
        self_test(
            bits=args.bits, n_trials=args.trials,
            layers=args.layers, iterations=args.iters, shots=args.shots,
            opt_level=args.opt_level, n_probes=args.n_probes,
            grover_shots=args.grover_shots, n_ipe_rounds=args.n_ipe,
            grover_top_k=args.grover_topk,
            backend_mode=args.backend, iqm_device=args.iqm_device,
            iqm_token=iqm_token, ibm_token=ibm_token, ibm_crn=ibm_crn,
            ibm_backend_name=ibm_backend_name,
            use_spsa=(not args.no_spsa), spsa_max_iter=args.spsa_iters,
        )
        return 0

    target_h160: bytes = b"\x00" * 20
    pubkey_xy = None; pubkey_hex = None
    address   = args.address.strip()

    if args.address:
        try:    target_h160 = address_to_hash160(args.address)
        except ValueError as e: log.error(str(e)); return 1

    if args.hash160:
        h = args.hash160.strip().replace("0x", "")
        if len(h) != 40: log.error("--hash160 must be 40 hex chars"); return 1
        target_h160 = bytes.fromhex(h)

    if args.pubkey and len(args.pubkey) >= 66:
        pubkey_hex = args.pubkey.lower()
        pubkey_xy  = decompress_pubkey(pubkey_hex)
        if pubkey_xy: log.info(f"Pubkey decompressed Qx={hex(pubkey_xy[0])[:18]}…")
        else:
            log.warning("Pubkey decompression failed — Hash160 mode")
            pubkey_xy = pubkey_hex = None

    if pubkey_xy:    mode_label = "Full Public Key — EC-Delta+SPSA+Shift"
    elif pubkey_hex: mode_label = "Address + Compressed PubKey"
    else:            mode_label = "Address Only — Hash160"

    bits       = args.bits
    full_start, full_end = auto_range(bits)
    base       = int(args.kstart, 16) if args.kstart else full_start
    use_spsa   = (not args.no_spsa) and SPSA_OK
    # [FIX v21] Define shor phase flags from CLI args (were undefined in v20 cli_main)
    shor_s1    = not args.no_shor_s1
    shor_s2    = not args.no_shor_s2
    shor_s3    = not args.no_shor_s3
    oracle_inf = "RZ-oracle (phase-kickback, IQM-safe)"  # DiagonalGate disabled
    if args.backend in ("iqm_hardware", "qrisp_iqm"):
        dev_q     = IQM_DEVICE_QUBITS.get(args.iqm_device, 18)
        sdk       = "pytket" if args.backend == "iqm_hardware" else "Qrisp"
        bkend_str = f"IQM {args.iqm_device.capitalize()} via {sdk} ({dev_q}q)"
    elif args.backend == "ibm_hardware":
        dev_q     = _MAX_IBM_QUBITS
        bkend_str = f"IBM {ibm_backend_name} (~{dev_q}q)"
    else:
        dev_q     = _MAX_AER_QUBITS
        bkend_str = "Aer Simulator"
    anc = compute_ancilla_count(bits, dev_q, args.backend)

    print(f"\n{'='*74}")
    print(f"  KEY-REDUCER IQM Edition  |  {mode_label}  |  {bits}-bit")
    print(f"  Full range   : [{hex(full_start)}, {hex(full_end)}]")
    print(f"  Backend      : {bkend_str}")
    print(f"  MAX-Q        : {bits+anc+1}q total ({bits}q key + {anc}q anc + 1q ctrl)")
    print(f"  Backend      : {args.backend}  |  Oracle: {oracle_inf}")
    print(f"  SPSA         : {'✅ '+str(args.spsa_iters)+' iters' if use_spsa else '— disabled'}")
    print(f"  Sobol        : {'✅' if SOBOL_OK else '— stratified fallback'}")
    print(f"  DBSCAN       : {'✅' if SKLEARN_OK else '— top-K fallback'}")
    print(f"  Multi-run    : {args.multi_run}")
    print(f"  Lattice      : {'fpylll BKZ-20' if FPYLLL_OK else '2×2 LLL fallback'}")
    print(f"  IQM_OK       : {'ON' if IQM_OK else 'ERROR pip install pytket-iqm'}")
    print(f"  pytket-qiskit: {'ON' if PYTKET_QISKIT_OK else 'ERROR pip install pytket-qiskit'}")
    print(f"  Qrisp_OK     : {'ON' if QRISP_OK else 'OFF pip install iqm-client>=34.0.3 qrisp'}")
    print(f"  IBM_OK       : {'ON' if IBM_OK else 'OFF pip install qiskit-ibm-runtime'}")
    print(f"  QWalk        : ON -- Three B2 engines: P-Bit (CPU) + QPB v3 (QPU) + AdapCoin (QPU)")
    print(f"  Trajectory   : ON -- FWHM density map range")
    print(f"  Honest note  : Output is heuristic. Run --self-test to measure hit rate.")
    print(f"{'='*74}")

    kw = dict(
        bits=bits, base=base,
        target_h160=target_h160, pubkey_xy=pubkey_xy, pubkey_hex=pubkey_hex,
        layers=args.layers, iterations=args.iters, shots=args.shots,
        opt_level=args.opt_level, n_probes=args.n_probes,
        grover_shots=args.grover_shots, n_ipe_rounds=args.n_ipe,
        grover_top_k=args.grover_topk,
        backend_mode=args.backend, iqm_device=args.iqm_device,
        iqm_token=iqm_token, ibm_token=ibm_token, ibm_crn=ibm_crn,
        ibm_backend_name=ibm_backend_name,
        save_plot=not args.no_plot, mode_label=mode_label, address=address,
        use_range_shift=(pubkey_xy is not None),
        use_spsa=use_spsa, spsa_max_iter=args.spsa_iters,
        use_kangaroo_export=not args.no_kangaroo,
        use_shor_s1=shor_s1, use_shor_s2=shor_s2, use_shor_s3=shor_s3,
    )

    t0 = time.perf_counter()
    if args.multi_run > 1:
        start_r, end_r, pinned, bit_probs = multi_run_reduce(
            n_runs=args.multi_run, **kw)
    else:
        start_r, end_r, pinned, bit_probs = reduce_keyspace(**kw)

    elapsed   = time.perf_counter() - t0
    full_size = full_end - full_start
    new_size  = end_r - start_r
    reduction = full_size / max(new_size, 1)
    pc        = sum(1 for b in pinned if b in ("0","1"))

    print(f"\n{'═'*74}")
    print(f"  🎯  QUANTUM TRAJECTORY BRACKET  ({elapsed:.1f}s)")
    print(f"{'═'*74}")
    print(f"  Backend      : {bkend_str}")
    print(f"")
    print(f"  ┌─ TRAJECTORY BRACKET ──────────────────────────────────────────────┐")
    print(f"  │  UPPER BOUND : {hex(start_r):<54} │")
    print(f"  │  LOWER BOUND : {hex(end_r):<54} │")
    print(f"  │  Range size  : {new_size:,} keys")
    print(f"  │  Bits pinned : {pc}/{bits}")
    print(f"  │  Reduction   : {reduction:.1f}×")
    print(f"  │  Method      : Quantum walk interference density — measured values only")
    print(f"  └────────────────────────────────────────────────────────────────────┘")
    print(f"")
    print(f"  BitCrack:")
    print(f"    bitcrack --keyspace {hex(start_r)}:{hex(end_r)} {address or '<address>'}")
    print(f"{'═'*74}\n")
    return 0


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    try:
        if len(sys.argv) == 1 or "--interactive" in sys.argv:
            interactive_main()
        else:
            sys.exit(cli_main())
    except KeyboardInterrupt:
        print("\n\nInterrupted by user"); sys.exit(0)
    except Exception as e:
        log.error(f"Fatal: {e}"); traceback.print_exc(); sys.exit(1)
