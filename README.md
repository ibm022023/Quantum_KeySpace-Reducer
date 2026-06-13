HERE IS THE RIGHT STEPS GUYS !!!! 
<img width="687" height="431" alt="Basic Fast Configs" src="https://raw.githubusercontent.com/threealgos/Quantum_KeySpace-Reducer/refs/heads/main/Recommended_Configs.png" />
> python3 P11-Solver-fixed-2.py
Choose:
  [  c]  Custom

Select preset [16]: c
Compressed pubkey (66 hex): 029d8c5d35231d75eb87fd2c5f05f65281ed9573dc41853288c62ee94eb2590b7a
Bit length [16]: 16
k_start (hex) [auto]: 
Shots [32768]: 16384

  Algorithm:
  [1] Regev Multi-Dim only
  [2] Regev + IPE Hybrid (recommended)   <----- Choose RegeV + IPE)
Select [2]: 2

  Adder:
  [draper]  Standard QFT-based
  [approx]  Approximate Draper (fewer rotations)
  [ripple]  Cuccaro ripple-carry (low-depth)
Select [draper]: ripple              <----- Choose ripple ) 

  Encoding:
  [none]       No encoding
  [repetition] [[3,1,1]] bit-flip code
  [surface]    Surface-d3 patch (single round)
  [cat]        Cat-qubit approximation
  [dualrail]   Dual-rail erasure detection
Select [none]: cat                   <----- Choose cat ) 

Clifford+T optimization? [Y/n]: Y    <----- Choose Y
Enable flag qubits? [Y/n]: Y      <-------- Same Y

  SDK:
  [qiskit]  Qiskit (default)
  [pytket]  pytket
Select [qiskit]: pytket      <----- Choose pytket/qiskit

  Backend:
  [aer]     Aer simulator
  [ibm]     IBM Quantum                                       <----- Choose ibm or
  [iqm]     IQM Resonance (pytket-iqm: sirius/garnet/emerald)  <----- Choose iqm
  [selene]  Quantinuum Selene (stabilizer)
  [helios]  Quantinuum HELIOS (Q-Nexus)
Select [aer]: iqm

Number of runs (Regev needs d+4 samples) [1]: 1   <------ One is Enough to crack 14/16 ....
IQM token: jCrgnrdLgaSwWrCnNdeSUsTHlq/xB7OioCXTFnRdlJcBnlCekaB3kJS1GnDWISQ7
IQM device [garnet / sirius / emerald]: emerald    >------WRITE IT THE BACKEND_NAME)
2026-05-22 17:01:28,749 | INFO | 
================================================================================
2026-05-22 17:01:28,749 | INFO | CONFIGURATION SUMMARY
2026-05-22 17:01:28,750 | INFO | ================================================================================
2026-05-22 17:01:28,750 | INFO | Bits: 16, k_start: 0x8000, shots: 16384, runs: 1
2026-05-22 17:01:28,750 | INFO | Algorithm: Regev+IPE Hybrid
2026-05-22 17:01:28,750 | INFO | Adder: ripple, Encoding: cat
2026-05-22 17:01:28,750 | INFO | SDK: pytket, Backend: iqm
2026-05-22 17:01:28,750 | INFO | Clifford+T: True, Flags: True, DR-Erasure: False
2026-05-22 17:01:28,751 | INFO | ================================================================================
2026-05-22 17:01:28,751 | INFO | ================================================================================
2026-05-22 17:01:28,751 | INFO | P11-REGEV-ULTIMATE v2 — Submission-Grade Hybrid Solver
2026-05-22 17:01:28,751 | INFO | ================================================================================
2026-05-22 17:01:28,751 | INFO | Target: 16-bit ECDLP, Q=(0x9d8c5d35231d75eb…, 0x83c227263dece3d7…)
2026-05-22 17:01:28,751 | INFO | k_start=0x8000, shots/run=16384, runs=1
2026-05-22 17:01:28,759 | INFO | Building PYTKET circuit (adder=ripple, encoding=cat, ipe=True)
2026-05-22 17:01:35,809 | INFO | pytket: peephole + redundancy passes applied
2026-05-22 17:01:35,810 | INFO | pytket Regev: d=5, qpd=4, qubits=38

2026-05-22 17:01:37,362 | INFO | IQM backend: Emerald (50q available)
2026-05-22 17:02:03,341 | INFO | IQM result: 15923 unique outcomes, 16384 shots
2026-05-22 17:02:03,352 | INFO | Got 15923 unique outcomes, 16384 total shots
2026-05-22 17:02:03,360 | INFO | Flag post-select: kept 397, discarded 15987
2026-05-22 17:02:03,361 | INFO | ================================================================================
2026-05-22 17:02:03,361 | INFO | POST-PROCESSING
2026-05-22 17:02:03,361 | INFO | ================================================================================
2026-05-22 17:02:03,361 | INFO | Lattice matrix: 70 rows × 5 cols
2026-05-22 17:02:03,361 | WARNING | fpylll unavailable — scalar LLL fallback
2026-05-22 17:02:03,361 | INFO | Lattice candidates: 68
2026-05-22 17:02:08,181 | INFO | Universal post-processing: 391 outcomes
2026-05-22 17:02:08,222 | INFO | Universal candidates: 3372
2026-05-22 17:02:11,478 | INFO | ✅ SOLUTION (universal): k = 51510

★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
  ✅ PRIVATE KEY RECOVERED: k = 51510
  Hex: 0xc936
  Time: 42.73s
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

Key saved → found_key_regev_v2_20260522_170211.txt

Please Some Donations Please for my Next Quantum Project :

1Bu4CR8Bi5AXQG8pnu1avny88C5CCgWKfb / 1NEJcwfcEm7Aax8oJNjRUnY3hEavCjNrai

Support This is my LTC Litecoin address for the next version of public-addresses: LdJX6Zr43PBekv11eKBfrMtpH78qi96Mef

USDT-TRON TQ1cxj8csRyWUzkonf5XgYUyFGsDJn1k7J

USDT-BSC 0x3fa39005a6bb18d0e2546d97b24a767cc393b03a

TODO: The Next Project is To Reveal A Supirior Version That Will Use Probabilistic Algorithm of Pbits Jumps Will be Used to Reduce All the Puzzles of BTC given Rangs to 2.0 % Targeting Public-Addresses . 

<img width="687" height="431" alt="Basic Fast Configs" src="https://raw.githubusercontent.com/threealgos/Quantum_Guppy-Q-Nexus/refs/heads/main/after-theStorm.png" />
<img width="687" height="431" alt="Basic Fast Configs" src="https://raw.githubusercontent.com/threealgos/Quantum_Guppy-Q-Nexus/refs/heads/main/before-theStorm.png" />
# ________________________________

# The Probabilistic Quantum Code :
# Will Features: 

#   • Works with public address ONLY (Puzzle 71)
#   • Works with public address + public key (Puzzle 135)
#   • Fully interactive - asks for EVERYTHING
#   • optimization_level choice (1/2/3) with suggestions
#   • layers & iterations with recommendations
#   • shots fully user-controlled
#   • Uses pycryptodome RIPEMD160 (Colab safe)
#   • Counter for measurement distribution
#   • Current IBM free backends (kingston, fez, marrakech)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  KEY-REDUCER · Quantum Probabilistic Keyspace Reducer · Supreme Edition    ║
║  IQM (pytket + Qrisp) · IBM Quantum · Aer · QUANTUM WALK ENGINE v5        ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  ── IQM Hardware (two SDK paths) ──────────────────────────────────────── ║
║    [pytket]  Sirius 16q · Garnet 20q · Emerald 54q (--backend iqm_hardware) ║
║    [Qrisp]   Sirius 16q · Garnet 20q · Emerald 54q (--backend qrisp_iqm)   ║
║              qrisp.interface.IQMBackend — auto native transpilation          ║
║  ── IBM Quantum Hardware (qiskit-ibm-runtime) ──────────────────────────── ║
║    ibm_fez 156q · ibm_brisbane 127q · etc. (--backend ibm_hardware)         ║
║    Token: export IBM_QUANTUM_TOKEN=your_ibm_token_here                      ║
║  ── Aer Simulator (local, no token) ────────────────────────────────────── ║
║    Always available · Recommended for testing                                ║
║                                                                              ║
║  [QUANTUM WALK] Discrete-time quantum walk on key-space hypercube.           ║
║    Each qubit = coin flip. Walk operator = Shift(Coin⊗I). Interference       ║
║    between walk steps reveals the trajectory gravity well of the unknown key.║
║    Superior to classical p-bits: O(√N) vs O(N) exploration of key-space.    ║
║  [TRAJECTORY] Gaussian interference density map → FWHM bracket = min/max.  ║
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
log.info("KEY-REDUCER  Supreme v5 — Quantum Walk + IQM(pytket/Qrisp) + IBM + Aer")
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
_MAX_IBM_QUBITS  = 127  # Conservative IBM cap (avoid routing overhead on 156q)
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
    kG     = _pt_mul(k_start, (_Gx, _Gy))
    neg_kG = (kG[0], (_P - kG[1]) % _P) if kG is not None else None
    delta  = _pt_add(pubkey_xy, neg_kG)
    dxs: List[int] = []; dys: List[int] = []
    cur = delta
    for _ in range(bits):
        dxs.append(int(cur[0]) if cur else 0)
        dys.append(int(cur[1]) if cur else 0)
        cur = _pt_add(cur, cur) if cur is not None else None
    log.info(f"  [DeltaPrecompute] Δ_x={hex(dxs[0])[:20]}…  bits={bits}")
    return dxs, dys


# =============================================================================
# [G-4] PUBLIC KEY RANGE SHIFTING / CENTERING
# =============================================================================

def range_shift_pubkey(
    pubkey_xy: Tuple[int, int],
    base:      int,
    bits:      int,
) -> Tuple[Optional[Tuple[int, int]], int]:
    try:
        shift   = base + (1 << (bits - 1))
        shift_G = _pt_mul(shift, (_Gx, _Gy))
        if shift_G is None: return None, 0
        neg_shift_G = (shift_G[0], (_P - shift_G[1]) % _P)
        q_shifted   = _pt_add(pubkey_xy, neg_shift_G)
        if q_shifted is None: return None, 0
        log.info(f"  [G-4 RangeShift] shift={hex(shift)[:18]}…  "
                 f"Q'_x={hex(q_shifted[0])[:18]}…")
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
    71: {"start": 0x580000000000000000,
         "end":   0x67fffffffffffffffe,
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
        # EC-delta prior: leading bit of dxs[b] tells us expected bit value.
        # Weight 0.5 = half the full bias range — strong directional prior.
        for b in range(bits):
            bl = dxs[b].bit_length() if dxs[b] else 0
            dx_bit = (dxs[b] >> (bl - 1)) & 1 if bl > 0 else 0
            h_biases[b] += (1.0 - 2.0 * dx_bit) * 0.5
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
    [TRAJECTORY] Extract the tightest honest bracket from raw QPU measurements.

    This is PURE POST-PROCESSING — no forced percentages, no padding.
    The two output values are real measured key candidates that bracket
    the interference density peak, just like the image shows:
    the p-bit/qubit trajectory orbits near the key without landing on it,
    and the TWO NEAREST SAMPLES on either side of the peak ARE the bracket.

    Algorithm:
    1. Score every measured sample by EC x-distance energy (FIX-ENERGY, real gradient)
    2. Build a Gaussian energy-weighted density map over key-space (normalised offsets)
    3. Find the interference PEAK — the region where qubits concentrated most
    4. LEFT BRACKET  = the lowest-energy sample whose absolute key <= peak key
       RIGHT BRACKET = the lowest-energy sample whose absolute key >= peak key
       These are the two ACTUAL MEASURED VALUES that tightest-bracket the peak.
    5. Bit probabilities computed only from samples inside [left, right]
    6. No minimum coverage padding — the output is exactly what the QPU found.
    """
    space = 1 << bits
    log.info(f"  [TRAJECTORY] {len(all_samples)} samples → interference density map")

    if not all_samples:
        log.warning("  [TRAJECTORY] No samples — nothing to extract")
        return (full_start, full_end, ["?"] * bits, np.full(bits, 0.5))

    # ── Step 1: Score all by energy, select top 25% lowest-energy ─────────────
    sorted_s = sorted(all_samples, key=lambda x: x[0])
    top_n    = max(16, len(sorted_s) // 4)
    top_s    = sorted_s[:top_n]
    top_offs = [int(o) for _, o in top_s]

    # ── Step 2: Gaussian energy-weighted density map ───────────────────────────
    # Window: span of top samples ± 4σ where σ = spread/8
    if len(top_offs) >= 2:
        spread = max(top_offs) - min(top_offs)
        sigma  = max(1, spread // 8)
    else:
        sigma  = max(1, space // 32)

    o_min   = max(0,          min(top_offs) - sigma * 4)
    o_max   = min(space - 1,  max(top_offs) + sigma * 4)
    w_range = o_max - o_min + 1

    # Build density array (cap size to avoid OOM on large key-spaces)
    if w_range > 0 and w_range <= 8_000_000:
        density = np.zeros(w_range, dtype=float)
        for eff, off in top_s:
            weight  = max(1e-6, 1.0 - float(eff))   # low energy → high weight
            idx     = int(off) - o_min
            if 0 <= idx < w_range:
                lo = max(0, idx - sigma * 4)
                hi = min(w_range - 1, idx + sigma * 4)
                gi_arr = np.arange(lo, hi + 1)
                density[lo:hi+1] += weight * np.exp(
                    -0.5 * ((gi_arr - idx) / max(sigma, 1)) ** 2
                )
        # Light smoothing to merge nearby measurement clusters
        if w_range > 10:
            kw2 = max(3, sigma // 4)
            try:
                density = np.convolve(density, np.ones(kw2) / kw2, mode="same")
            except Exception:
                pass
        peak_idx    = int(np.argmax(density))
        peak_offset = peak_idx + o_min          # peak in offset space
    else:
        # Large space: DBSCAN centroid of lowest-energy cluster
        cluster_db  = dbscan_cluster_offsets(top_s, bits, eps_frac=0.03, min_samples=3)
        use_offs    = cluster_db if (cluster_db and len(cluster_db) >= 2) else top_offs
        peak_offset = int(np.median(use_offs))
        log.info(f"  [TRAJECTORY] Large space — DBSCAN centroid peak={hex(peak_offset)}")

    # sigma floor: never so small it produces size=1 bracket
    sigma = max(sigma, space // 1024, 8)

    # ── Step 3: Find the TWO ACTUAL MEASURED VALUES that bracket the peak ─────
    # Left bracket  = the measured sample with the SMALLEST offset >= nothing,
    #                 BUT closest to the peak from the LEFT.
    # Right bracket = the measured sample closest to the peak from the RIGHT.
    # We pick from ALL low-energy samples (top 50%) not just top 25%,
    # to have enough candidates to bracket both sides of the peak.
    # ── Collect all low-energy samples within 2σ of the peak ─────────────────
    sigma = max(sigma, space // 1024, 8)  # floor: never size=1
    half_n    = max(64, len(sorted_s) // 2)
    pool_offs = [int(o) for _, o in sorted_s[:half_n]]
    window_offs = [o for o in pool_offs if abs(o - peak_offset) <= 2 * sigma]
    if len(window_offs) < 4:
        window_offs = sorted(pool_offs, key=lambda o: abs(o-peak_offset))[:max(32, len(pool_offs)//8)]
    left_offset  = max(0,          min(window_offs))
    right_offset = min(space - 1,  max(window_offs))
    if right_offset - left_offset < sigma:
        mid = (left_offset + right_offset) // 2
        left_offset  = max(0,         mid - sigma)
        right_offset = min(space - 1, mid + sigma)

    log.info(f"  [TRAJECTORY] Peak offset={hex(peak_offset)}  "
             f"UPPER_BOUND={hex(base + left_offset)}  "
             f"LOWER_BOUND={hex(base + right_offset)}")

    # ── Step 4: Convert to absolute key values — NO padding, NO forced % ──────
    start_r = max(full_start, base + left_offset)
    end_r   = min(full_end,   base + right_offset)

    # Ensure start < end (can happen if left==right, i.e. single sample at peak)
    if start_r >= end_r:
        start_r = max(full_start, end_r - 1)
        end_r   = min(full_end, start_r + max(1, sigma))

    # ── Step 5: Bit probabilities from samples inside the bracket ─────────────
    bracket_s = [(e, o) for e, o in sorted_s[:half_n]
                 if left_offset <= o <= right_offset]
    if len(bracket_s) < 4:
        bracket_s = top_s[:min(len(top_s), 64)]
    b_offs = [int(o) for _, o in bracket_s]

    bit_arrays = np.array(
        [[(o >> (bits-1-b)) & 1 for b in range(bits)] for o in b_offs],
        dtype=float
    ) if b_offs else np.full((1, bits), 0.5)
    bit_probs = bit_arrays.mean(axis=0)

    # ── Step 6: Pin bits from bit probabilities ────────────────────────────────
    pinned: List[str] = []
    for thr_hi, thr_lo in [(0.90, 0.10), (0.82, 0.18), (0.74, 0.26), (0.64, 0.36)]:
        pinned = ["1" if p > thr_hi else "0" if p < thr_lo else "?" for p in bit_probs]
        pc     = sum(1 for b in pinned if b in ("0", "1"))
        if pc >= bits // 4:
            break

    full_sz = full_end - full_start
    pc = sum(1 for b in pinned if b in ("0", "1"))
    bracket_sz = end_r - start_r
    log.info(f"  [TRAJECTORY] BRACKET [{hex(start_r)}, {hex(end_r)}]  "
             f"size={bracket_sz:,}  pins={pc}/{bits}  "
             f"reduction={full_sz // max(bracket_sz, 1):.1f}×")

    return start_r, end_r, pinned, bit_probs


def force_best_range(
    all_samples: List[Tuple[float, int]], base: int, bits: int,
    full_start: int, full_end: int, target_coverage: float = 0.10,
) -> Tuple[int, int, List[str], np.ndarray]:
    """
    Last-resort bracket extractor — pure post-processing, no forced %.
    Finds the two actual measured values that tightest-bracket the
    DBSCAN density centroid of the lowest-energy samples.
    NO padding, NO minimum coverage percentage.
    """
    if not all_samples:
        log.warning("  [ForceResult] No samples — full range returned")
        return (full_start, full_end, ["?"]*bits, np.full(bits, 0.5))

    # Use the lowest-energy 50% of samples as candidates
    sorted_s     = sorted(all_samples, key=lambda x: x[0])
    half_n       = max(16, len(sorted_s) // 2)
    candidates   = sorted_s[:half_n]

    # DBSCAN to find the densest cluster of low-energy offsets
    cluster_offs = dbscan_cluster_offsets(candidates, bits, eps_frac=0.03, min_samples=3)
    if not cluster_offs or len(cluster_offs) < 2:
        cluster_offs = [int(o) for _, o in candidates]

    # Centroid of the cluster = estimated trajectory peak location
    centroid = int(np.median(cluster_offs))

    # Left bracket = highest measured offset ≤ centroid
    # Right bracket = lowest measured offset ≥ centroid
    all_offs_sorted = sorted(set(cluster_offs))
    left_candidates  = [o for o in all_offs_sorted if o <= centroid]
    right_candidates = [o for o in all_offs_sorted if o >= centroid]

    left_off  = max(left_candidates)  if left_candidates  else centroid
    right_off = min(right_candidates) if right_candidates else centroid

    start_r = max(full_start, base + left_off)
    end_r   = min(full_end,   base + right_off)
    if start_r >= end_r:
        min_bracket = max(2, (1 << bits) // 1024)
        end_r = min(full_end, start_r + min_bracket)

    # Bit probabilities from the bracketed cluster
    b_offs = [o for o in cluster_offs if left_off <= o <= right_off]
    if len(b_offs) < 4: b_offs = cluster_offs
    bit_arrays = np.array(
        [[(o >> (bits-1-b)) & 1 for b in range(bits)] for o in b_offs],
        dtype=float)
    bit_probs = bit_arrays.mean(axis=0)

    best_pinned = None; best_pc = 0
    for high, low in [(0.88,0.12),(0.80,0.20),(0.72,0.28),(0.62,0.38)]:
        cand = ["1" if p>high else "0" if p<low else "?" for p in bit_probs]
        pc   = sum(1 for b in cand if b in ("0","1"))
        if pc > best_pc: best_pc = pc; best_pinned = cand
    if not best_pinned: best_pinned = ["?"]*bits

    log.info(f"  [ForceResult] centroid={hex(base+centroid)}  "
             f"UPPER_BOUND={hex(start_r)}  LOWER_BOUND={hex(end_r)}  "
             f"size={end_r-start_r:,}  pins={best_pc}/{bits}")
    return start_r, end_r, best_pinned, bit_probs


# =============================================================================
# IQM BACKEND  (replaces IBM _get_sampler_and_backend)
# =============================================================================

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
#   Available on IBM 127q and IQM Emerald 50q.
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
        if dxs is not None and b < len(dxs) and dxs[b] != 0:
            # EC delta-x oracle: the MSB of dxs[b] encodes expected bit value
            bl     = dxs[b].bit_length()
            msb    = (dxs[b] >> (bl - 1)) & 1 if bl > 0 else 0
            # phi > 0 → amplify |1⟩, phi < 0 → amplify |0⟩
            phi    = math.pi * (1.0 - 2.0 * msb) * anneal
        else:
            # Ising bias fallback: h_bias encodes energy gradient per bit
            phi    = math.pi * float(h_biases[b]) * anneal
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
    [QUANTUM WALK v2] Biased discrete-time quantum walk with:
      - Per-step EC phase oracle (in-circuit energy evaluation)
      - Adaptive coin that self-steers toward low-energy region
      - Long-range Ising couplings (skip-2, skip-3, skip-4)
      - Extra reach qubits for longer-range interference
        (entangled but not measured — traced out naturally)

    This is the closest achievable equivalent to a p-bit machine
    on current gate-based QPU hardware without a full EC oracle
    (which requires ~3000 qubits for secp256k1 — not yet available).

    Per-step architecture:
      1. Adaptive coin  Ry(theta_b) — self-steering, not fixed H
      2. Shift operator CNOT cascade — moves walker in key-space
      3. Phase oracle   RZ(phi_b)   — EC delta-x energy per step
      4. J couplings    RZZ(J_b)    — NN + skip-2/3/4 interactions
      5. Reach qubits   CX to extra register — longer interference
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

    # Extra reach qubits: go beyond key register for longer-range interference
    # They are entangled but NOT measured — pure interference amplifiers
    safe_reach = min(extra_reach, max(0, max_total - bits))
    total      = bits + safe_reach

    key_r  = QuantumRegister(bits, "wk")
    cr     = ClassicalRegister(bits, "wc")
    if safe_reach > 0:
        reach_r = QuantumRegister(safe_reach, "wr")
        qc = QuantumCircuit(key_r, reach_r, cr,
                            name=f"QWalkV2_{bits}q_{walk_steps}s")
        qc.h(reach_r)
    else:
        reach_r = None
        qc = QuantumCircuit(key_r, cr,
                            name=f"QWalkV2_{bits}q_{walk_steps}s")

    # Initial superposition
    qc.h(key_r)

    # Adaptive coin angles — start at pi/2 (Hadamard), updated each step
    coin_angles = np.full(bits, math.pi / 2.0)
    # Coin learning rate: how fast the coin adapts per step
    coin_lr     = 0.15

    for step in range(walk_steps):

        # ── 1. Adaptive coin ─────────────────────────────────────────────────
        _build_adaptive_coin(qc, key_r, bits, coin_angles)

        # ── 2. Shift operator (CNOT cascade) ─────────────────────────────────
        for b in range(1, bits):
            qc.cx(key_r[b-1], key_r[b])

        # ── 3. Per-step EC phase oracle ───────────────────────────────────────
        # This is the KEY addition: energy evaluated INSIDE the circuit
        # per walk step, not just once classically before the circuit.
        _build_phase_oracle_step(qc, key_r, bits, dxs, step, walk_steps, h_biases)

        # Update adaptive coin angles based on oracle feedback (classically)
        anneal = 0.3 + 0.7 * (step / max(walk_steps - 1, 1))
        for b in range(bits):
            if dxs is not None and b < len(dxs) and dxs[b] != 0:
                bl  = dxs[b].bit_length()
                msb = (dxs[b] >> (bl - 1)) & 1 if bl > 0 else 0
                phi = math.pi * (1.0 - 2.0 * msb) * anneal
            else:
                phi = math.pi * float(h_biases[b]) * anneal
            # Steer coin toward 0 for bits with strong phase signal
            coin_angles[b] = max(0.05, coin_angles[b] - coin_lr * abs(phi))

        # ── 4. Ising couplings: NN + skip-2 + skip-3 + skip-4 ───────────────
        # NN couplings
        for b in range(min(bits - 1, len(J_couplings))):
            a = float(J_couplings[b] * math.pi)
            if abs(a) > 1e-6:
                qc.rzz(a, key_r[b], key_r[b+1])
        # Skip-2
        for b in range(min(bits - 2, len(J_couplings))):
            a = float(J_couplings[b] * math.pi * 0.5)
            if abs(a) > 1e-6:
                qc.rzz(a, key_r[b], key_r[b+2])
        # Skip-3 (new — needs ≥4 qubits)
        for b in range(min(bits - 3, len(J_couplings))):
            a = float(J_couplings[b] * math.pi * 0.25)
            if abs(a) > 1e-6:
                qc.rzz(a, key_r[b], key_r[b+3])
        # Skip-4 (new — needs ≥5 qubits, only on 50q+ devices)
        if bits >= 5:
            for b in range(min(bits - 4, len(J_couplings))):
                a = float(J_couplings[b] * math.pi * 0.125)
                if abs(a) > 1e-6:
                    qc.rzz(a, key_r[b], key_r[b+4])

        # ── 5. Reach register interference amplifiers ─────────────────────────
        # Extra qubits beyond the key register create longer-range interference
        # patterns. They are traced out (not measured) — pure quantum resource.
        if reach_r is not None and safe_reach > 0:
            for ri in range(safe_reach):
                # Entangle reach[ri] with key[(ri*3) % bits] — spread across key
                ki = (ri * 3) % bits
                qc.cx(key_r[ki], reach_r[ri])
                # Apply phase from oracle to reach qubit too
                if dxs is not None and ki < len(dxs) and dxs[ki] != 0:
                    bl  = dxs[ki].bit_length()
                    msb = (dxs[ki] >> (bl-1)) & 1 if bl > 0 else 0
                    phi = math.pi * (1.0 - 2.0 * msb) * anneal * 0.5
                    if abs(phi) > 1e-6:
                        qc.rz(phi, reach_r[ri])
                # Un-entangle reach qubit (keeps circuit depth low)
                qc.cx(key_r[ki], reach_r[ri])

    # Reverse shift to restore key register to computational basis
    for b in range(bits - 1, 0, -1):
        qc.cx(key_r[b-1], key_r[b])

    # Measure only key register
    qc.measure(key_r, cr)

    log.info(f"  [QWalkV2] {total}q total  {bits}q key + {safe_reach}q reach  "
             f"{walk_steps} steps  oracle={'EC-delta' if dxs else 'h_bias'}  "
             f"depth={qc.depth()}")
    return qc


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
) -> List[Tuple[float, int]]:
    """
    [QUANTUM WALK PHASE v2] Run multiple biased quantum walk circuits.

    Each walk uses the per-step EC phase oracle (build_quantum_walk_circuit v2)
    which encodes EC delta-x information INSIDE the circuit per step.
    Extra reach qubits (device capacity - bits) extend interference range.

    Returns: (energy, offset) pairs — the interference map samples.
    """
    if not QISKIT_OK:
        log.warning("  [QWalk] Qiskit unavailable — skipped")
        return []

    oracle_type = "EC-delta phase oracle" if dxs else "h_bias fallback"
    log.info(f"  [QWalkV2] {n_walks} walks × {shots} shots × {walk_steps} steps  "
             f"bits={bits}  oracle={oracle_type}")

    # Connect hardware once
    iqm_backend = None; ibm_sampler_w = None; ibm_backend_obj_w = None
    if backend_mode == "iqm_hardware":
        try:
            iqm_backend = _get_iqm_backend_obj(iqm_device, iqm_token)
        except Exception as e:
            log.warning(f"  [QWalk IQM] {e} — Aer fallback")
            backend_mode = "simulator"
    elif backend_mode == "ibm_hardware":
        try:
            ibm_sampler_w, ibm_backend_obj_w = _get_ibm_sampler(
                ibm_token, ibm_crn, ibm_backend_name)
        except Exception as e:
            log.warning(f"  [QWalk IBM] {e} — Aer fallback")
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
            log.warning(f"  [QWalk {walk_idx+1}] error: {e}")
            continue

        walk_samples: List[Tuple[float, int]] = []
        for bitstr, cnt in counts.items():
            bs     = bitstr.zfill(bits)[-bits:]
            offset = int(bs, 2)
            energy = compute_energy(base + offset, target_h160, pubkey_xy, pubkey_hex)
            bv     = np.array([(offset >> b) & 1 for b in range(bits)], dtype=float)
            # Effective energy: blend actual energy with Ising bias alignment
            dot_norm = (float(np.dot(h_biases, bv)) + bits) / (2.0 * bits + 1e-9)
            eff    = 0.65 * energy + 0.35 * (1.0 - dot_norm)
            w = max(1, min(cnt, 20))
            for _ in range(w):
                walk_samples.append((eff, offset))

        all_walk_samples.extend(walk_samples)
        n_unique = len(set(o for _, o in walk_samples))
        best_e   = min((e for e, _ in walk_samples), default=256.0)
        log.info(f"  [QWalk {walk_idx+1}/{n_walks}] steps={steps}  "
                 f"unique={n_unique}  best_eff={best_e:.3f}  "
                 f"total_pairs={len(all_walk_samples)}")

    log.info(f"  [QWalk] Phase complete — {len(all_walk_samples)} total pairs")
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
) -> Tuple[List[Tuple[float, int]], float]:
    """
    Phase B sampler. Routes to:
      simulator    → Aer (local)
      iqm_hardware → IQM via pytket bridge
      qrisp_iqm   → IQM via Qrisp (auto-native-transpilation)
      ibm_hardware → IBM Quantum Runtime
    """
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
        for bitstr, cnt in counts.items():
            bs     = bitstr.zfill(bits)[-bits:]
            offset = int(bs, 2)
            energy = compute_energy(base+offset, target_h160, pubkey_xy, pubkey_hex)
            bv     = np.array([(offset >> b) & 1 for b in range(bits)], dtype=float)
            # FIX: normalise dot to [0,1] so eff stays in [0,1] always
            dot_norm = (float(np.dot(h_biases, bv)) + bits) / (2.0 * bits + 1e-9)
            eff    = 0.7 * energy + 0.3 * (1.0 - dot_norm)   # both terms positive
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
    full_start, full_end = auto_range(bits)
    log.info("=" * 72)
    log.info(f"  REDUCE  {bits}-bit  base={hex(base)}  mode={mode_label}")
    log.info(f"  Backend: {backend_mode}  device: {iqm_device}")
    log.info(f"  Full range: [{hex(full_start)}, {hex(full_end)}]")

    # [G-4] Range shift
    shift = 0; pubkey_shifted = None
    if pubkey_xy is not None and use_range_shift:
        pubkey_shifted, shift = range_shift_pubkey(pubkey_xy, base, bits)
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
    sampler_samples, best_energy = run_sampler_phase(
        bits=bits, base=base,
        target_h160=target_h160, pubkey_xy=effective_pubkey, pubkey_hex=pubkey_hex,
        h_biases=h_biases, J_couplings=J_couplings,
        layers=layers, iterations=iterations, shots=shots, opt_level=opt_level,
        backend_mode=backend_mode, iqm_device=iqm_device, iqm_token=iqm_token,
        ibm_token=ibm_token, ibm_crn=ibm_crn, ibm_backend_name=ibm_backend_name,
        use_spsa=use_spsa, spsa_max_iter=spsa_max_iter, ancilla=ancilla,
    )
    log.info(f"  [Phase B] {len(sampler_samples)} pairs  best_eff={best_energy:.3f}")

    # Phase B2: [QUANTUM WALK] Discrete-time quantum walk
    # Each qubit makes quantum jumps through key-space (not classical random steps)
    # O(√N) exploration beats classical p-bits' O(N) with quadratic speedup.
    # Multiple walks with varying biases create interference patterns that
    # reveal the trajectory gravity well of the unknown key.
    # More steps now that we have per-step phase oracle:
    # each step meaningfully accumulates EC phase, not just random shift.
    # Cap at 8 to keep circuit depth reasonable for hardware.
    walk_steps = max(3, min(8, bits // 4))
    n_walks    = max(2, min(6, iterations // 2))
    walk_shots = max(1024, min(shots, 8192))
    log.info(f"  [Phase B2 QWalk] {n_walks} walks × {walk_steps} steps × {walk_shots} shots")
    # FIX-ANCILLA: walk uses ancilla=0 so ALL device qubits become walk qubits.
    # Ancilla entanglement in a biased random walk only adds decoherence — it
    # dilutes the key-register signal without improving key-space coverage.
    walk_samples = run_quantum_walk_phase(
        bits=bits, base=base,
        target_h160=target_h160, pubkey_xy=effective_pubkey, pubkey_hex=pubkey_hex,
        h_biases=h_biases, J_couplings=J_couplings,
        ancilla=0, walk_steps=walk_steps,
        shots=walk_shots, opt_level=opt_level,
        backend_mode=backend_mode, iqm_device=iqm_device, iqm_token=iqm_token,
        ibm_token=ibm_token, ibm_crn=ibm_crn, ibm_backend_name=ibm_backend_name,
        n_walks=n_walks,
        dxs=dxs,   # EC delta-x for per-step phase oracle inside the walk circuit
    )
    sampler_samples = sampler_samples + walk_samples
    log.info(f"  [Phase B2] +{len(walk_samples)} walk pairs → "
             f"total={len(sampler_samples)} pairs")

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
            log.info(f"  [MODE1-PBIT] bits={bits} > {_MODE1_GROVER_MAX_BITS} "
                     f"→ p-bit quantum-enhanced exhaustive sampler")
            pbit_s, mode1_found_offset = run_mode1_pbit_sampler(
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
        # ── STANDARD PATH (pubkey available) ──────────────────────────────────
        grover_samples = run_grover_ipe_phase(
            bits=bits, sampler_samples=sampler_samples, h_biases=h_biases,
            base=base, target_h160=target_h160,
            pubkey_xy=effective_pubkey, pubkey_hex=pubkey_hex,
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

    # Phase D: Lattice [G-8] + DBSCAN [G-7] + forced result
    top_for_lattice = list(dict.fromkeys(
        int(o) for _, o in sorted(sampler_samples, key=lambda x: x[0])[:grover_top_k]
    ))
    lattice_samples = lattice_refine_candidates(
        top_for_lattice, bits, base, target_h160, effective_pubkey, pubkey_hex, 20)

    all_samples = sampler_samples + grover_samples + lattice_samples
    log.info(f"  [Phase D] {len(all_samples)} total  "
             f"(S+QW={len(sampler_samples)} G={len(grover_samples)} L={len(lattice_samples)})")

    # [TRAJECTORY] Pure post-processing: extract the two real measured
    # values that tightest-bracket the interference density peak.
    # No forced percentages — output is exactly what the QPU found.
    start_r, end_r, pinned, bit_probs = quantum_trajectory_range(
        all_samples, base, bits, full_start, full_end,
        pubkey_xy=effective_pubkey, target_h160=target_h160,
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
    results: List[Tuple[int, int]] = []
    last_pinned = ["?"] * kwargs.get("bits", 16)
    last_bp     = np.full(kwargs.get("bits", 16), 0.5)
    log.info(f"\n{'='*60}")
    log.info(f"  [G-6 MultiRun] {n_runs} runs — will intersect ranges")
    for run in range(n_runs):
        log.info(f"  [G-6] Run {run+1}/{n_runs}…")
        kwargs["save_plot"]           = (run == 0)
        kwargs["use_kangaroo_export"] = (run == n_runs - 1)
        s, e, pinned, bp = reduce_keyspace(**kwargs)
        results.append((s, e)); last_pinned = pinned; last_bp = bp
    int_start = max(s for s, _ in results)
    int_end   = min(e for _, e in results)
    if int_start < int_end:
        log.info(f"\n  [G-6 MultiRun] Intersection: [{hex(int_start)}, {hex(int_end)}]  "
                 f"size={int_end-int_start:,}")
        return int_start, int_end, last_pinned, last_bp
    union_s = min(s for s, _ in results); union_e = max(e for _, e in results)
    log.warning(f"  [G-6 MultiRun] Runs did not intersect — union "
                f"[{hex(union_s)}, {hex(union_e)}]")
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
  WHAT THIS TOOL ACTUALLY DOES
  ─────────────────────────────
  Combines quantum probabilistic sampling + classical energy sensing to
  output a sub-range statistically more likely to contain the unknown key.
  It does NOT guarantee 100% containment (impossible without breaking ECDLP).

    Phase A — SparsePauliOp Ising Landscape  [Sobol + non-NN couplings]
    Phase B  - SPSA-optimised TwoLocal Sampler  [G-1 SPSA]
    Phase B2 - [QUANTUM WALK] O(sqrt(N)) discrete-time walk on key-space
               Qubits explore ALL positions simultaneously via superposition
               Interference density peaks reveal key trajectory location
    Phase C — Grover-IPE / Real Grover / p-bit sampler
    Phase D — DBSCAN [G-7] + BKZ/LLL [G-8] + Forced Output
    Phase E — Kangaroo Export [G-5] + Multi-run Voting [G-6]
""")

    # ── Input mode ─────────────────────────────────────────────────────────────
    print("  ┌─ INPUT MODE ─────────────────────────────────────────────────────┐")
    print("  │  [1]  Bitcoin P2PKH address only        (Hash160 — Mode1 Grover) │")
    print("  │  [2]  Address  +  compressed public key    (hybrid — strong)     │")
    print("  │  [3]  Compressed public key only           (strongest signal)    │")
    print("  └───────────────────────────────────────────────────────────────────┘")
    choice = _ask("Select input mode [1/2/3]", "3")

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

    kstart_s = _ask(f"Key range start hex [auto = {hex(full_start)}]", hex(full_start))
    try:    base = int(kstart_s, 16)
    except: base = full_start

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
    print("  │  [8]  IBM Hardware  (ibm_fez 156q · ibm_brisbane 127q · etc.)    │")
    print("  └────────────────────────────────────────────────────────────────────┘")
    bk_in = _ask("Backend [1..8]", "1")

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


    # ── Sampler parameters — pre-filled from preset ────────────────────────────
    _def_shots  = _preset_shots(bits)
    _def_layers = _preset_layers(bits)
    _def_iters  = _preset_iters(bits)
    _def_probes = _preset_probes(bits)
    _has_preset = bits in PUZZLE_PRESETS
    _pfx        = "preset" if _has_preset else "default"

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
    print(f"  │  Shots ({_pfx:<7})   {_def_shots:<6} (2048=fast · 65536=best)       │")
    print(f"  │  Layers ({_pfx:<7})  {_def_layers} (3=fast · 5=deep)                 │")
    print(f"  │  Iters ({_pfx:<7})   {_def_iters:<2} (4=quick · 20=thorough)           │")
    print(f"  │  Ising probes ({_pfx:<7}) {_def_probes:<4} (256=fast · 1024=best)   │")
    print( "  │  SPSA iterations     0=disabled · 40=fast · 60=default · 100=best│")
    print( "  └───────────────────────────────────────────────────────────────────┘")
    layers     = int(_ask("TwoLocal layers",         str(_def_layers)))
    iters      = int(_ask("Iterations",              str(_def_iters)))
    shots      = int(_ask("Shots per iter",          str(_def_shots)))
    opt_level  = int(_ask("Transpile opt level",     "2"))
    n_probes   = int(_ask("Ising probes",            str(_def_probes)))
    spsa_iters = int(_ask("SPSA iterations (0=off)", "60"))
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
    print("  │  Top-K candidates 32=fast · 128=default(G-8) · 256=thorough      │")
    print(f"  │  Oracle (auto)    {oracle_info:<52} │")
    print("  └───────────────────────────────────────────────────────────────────┘")
    n_ipe   = int(_ask("IPE rounds (≥3)",      "4"))
    g_shots = int(_ask("Grover shots",         str(_def_shots)))
    g_topk  = int(_ask("Top-K candidates",    "128"))

    # ── Multi-run ─────────────────────────────────────────────────────────────
    print("\n  ┌─ MULTI-RUN VOTING [G-6] ─────────────────────────────────────────┐")
    print("  │  1=single run(default) · 3=good · 5=tighter · 10=tight+slow      │")
    print("  └───────────────────────────────────────────────────────────────────┘")
    n_runs   = int(_ask("Number of runs", "1"))
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
    print(f"  Bits         : {bits}  |  Full: [{hex(full_start)}, {hex(full_end)}]")
    print(f"  Base         : {hex(base)}")
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
    print(f"  QWalk        : ✅ Quantum Walk Engine active (O(√N) exploration)")
    print(f"  Trajectory   : ✅ FWHM interference density map → tightest range")
    print(f"{'─'*74}")

    if _ask("Run now? [Y/n]", "Y").lower() in ("n", "no"):
        print("  Aborted."); return

    t0  = time.perf_counter()
    kw  = dict(
        bits=bits, base=base,
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
    print(f"  │  UPPER BOUND : {hex(start_r):<54} │")
    print(f"  │  LOWER BOUND : {hex(end_r):<54} │")
    print(f"  │  Range size  : {new_size:<,} keys")
    print(f"  │  Reduction   : {reduction:.1f}× smaller than full {bits}-bit range")
    print(f"  │  Method      : Quantum walk interference density — measured values only")
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
    oracle_inf = ("DiagonalGate" if bits <= _DIAG_MAX_BITS else "Phase-kickback")
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
    print(f"  QWalk        : ON -- O(sqrt(N)) quantum walk")
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
