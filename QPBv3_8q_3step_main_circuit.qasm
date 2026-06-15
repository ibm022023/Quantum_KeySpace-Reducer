// ============================================================
// KEY-REDUCER · QPB Engine v3 · OpenQASM 3.0
// ============================================================
// Source : Q-Probabilistic_KeySpace_Reducer_Dwave.py  v21
// Circuit: build_quantum_walk_circuit()  — the MAIN common circuit
//          used in Phase B2 by run_quantum_walk_phase()
//          (QPB Engine v3 — one of the three pooled engines)
//
// Architecture — 8 qubits, 3 walk steps, β: 0.5 → 4.0
// ──────────────────────────────────────────────────────────────
// Register  qpb[0..7] — key-bit quantum P-Bit register
// Register  wc[0..7]  — classical measurement output
//
// Per-step structure (3 steps total):
//   STEP 1 — QPB gate per qubit
//     Ry(2·arcsin(√p_b))  where p_b = sigmoid(β · I_b)
//     I_b = h_biases[b] + EC-delta steering × anneal_progress
//     This is the EXACT quantum gate that produces P(|1⟩) = p_b
//     and is mathematically identical to the p-bit stochastic decision.
//
//   STEP 2 — CRZ neighbour coupling  (quantum W_ij matrix)
//     NN coupling    j = b±1  weight = J[b]  × β        (full)
//     skip-2 coupling j = b±2  weight = J[b]  × β × 0.5  (half)
//     skip-3 coupling j = b±3  weight = J[b]  × β × 0.25 (quarter)
//     CRZ(θ, ctrl, tgt): rotates tgt by θ if ctrl = |1⟩
//     Quantum equivalent of p-bit local field: I_i += W_ij · s_j
//
//   STEP 3 — EC phase oracle  RZ(φ_b) per qubit
//     φ_b from EC delta-x hints (dxs[b]) or h_biases[b]
//     Angle scales with annealing progress (0.3 + 0.7 × step/steps)
//     Steers phases toward correct key bits coherently.
//
// β annealing schedule (hot → cold):
//   β = 0.5  (step 0) → spread cloud (sigmoid ≈ 0.5, Ry ≈ π/2)
//   β = 4.0  (step 2) → committed snake (sigmoid → 0 or 1, Ry → 0 or π)
//
// Concrete parameters used (8-bit representative run):
//   h_biases    = [ 0.312, -0.187,  0.450, -0.063,
//                   0.275,  0.124, -0.338,  0.201 ]
//   J_couplings = [ 0.098, -0.142,  0.076, -0.055,
//                   0.113,  0.089, -0.067 ]
//   dxs (EC delta-x hints) = [1, 0, 1, 1, 0, 0, 1, 0]
//
// Gate summary:
//   h    ×  8   — hot start (uniform superposition)
//   ry   × 24   — QPB gate (p-bit sigmoid probability)
//   crz  × 108  — CRZ coupling (quantum W_ij)
//   rz   × 24   — EC phase oracle (energy steering)
//   measure × 8 — terminal measurement
//   Depth: 64
//
// Compatible with: Qiskit Aer, IBM Quantum, IQM (after pytket transpile)
// ============================================================

OPENQASM 3.0;
include "stdgates.inc";
bit[8] wc;
qubit[8] qpb;
h qpb[0];
h qpb[1];
h qpb[2];
h qpb[3];
h qpb[4];
h qpb[5];
h qpb[6];
h qpb[7];
ry(1.6487173548816365) qpb[0];
ry(1.5240633466706976) qpb[1];
ry(1.6830597702048624) qpb[2];
ry(1.5550469779185798) qpb[3];
ry(1.6394922321744358) qpb[4];
ry(1.6017913628207783) qpb[5];
ry(1.4863967061839518) qpb[6];
ry(1.621025192736301) qpb[7];
crz(0.049) qpb[0], qpb[1];
crz(0.049) qpb[1], qpb[0];
crz(-0.071) qpb[1], qpb[2];
crz(-0.071) qpb[2], qpb[1];
crz(0.038) qpb[2], qpb[3];
crz(0.038) qpb[3], qpb[2];
crz(-0.0275) qpb[3], qpb[4];
crz(-0.0275) qpb[4], qpb[3];
crz(0.0565) qpb[4], qpb[5];
crz(0.0565) qpb[5], qpb[4];
crz(0.0445) qpb[5], qpb[6];
crz(0.0445) qpb[6], qpb[5];
crz(-0.0335) qpb[6], qpb[7];
crz(-0.0335) qpb[7], qpb[6];
crz(0.0245) qpb[0], qpb[2];
crz(0.0245) qpb[2], qpb[0];
crz(-0.0355) qpb[1], qpb[3];
crz(-0.0355) qpb[3], qpb[1];
crz(0.019) qpb[2], qpb[4];
crz(0.019) qpb[4], qpb[2];
crz(-0.01375) qpb[3], qpb[5];
crz(-0.01375) qpb[5], qpb[3];
crz(0.02825) qpb[4], qpb[6];
crz(0.02825) qpb[6], qpb[4];
crz(0.02225) qpb[5], qpb[7];
crz(0.02225) qpb[7], qpb[5];
crz(0.01225) qpb[0], qpb[3];
crz(0.01225) qpb[3], qpb[0];
crz(-0.01775) qpb[1], qpb[4];
crz(-0.01775) qpb[4], qpb[1];
crz(0.0095) qpb[2], qpb[5];
crz(0.0095) qpb[5], qpb[2];
crz(-0.006875) qpb[3], qpb[6];
crz(-0.006875) qpb[6], qpb[3];
crz(0.014125) qpb[4], qpb[7];
crz(0.014125) qpb[7], qpb[4];
rz(-3*pi/10) qpb[0];
rz(3*pi/10) qpb[1];
rz(-3*pi/10) qpb[2];
rz(-3*pi/10) qpb[3];
rz(3*pi/10) qpb[4];
rz(3*pi/10) qpb[5];
rz(-3*pi/10) qpb[6];
rz(3*pi/10) qpb[7];
ry(1.6404898391338198) qpb[0];
ry(1.6416120638779295) qpb[1];
ry(1.7939215686149994) qpb[2];
ry(1.2257303615235042) qpb[3];
ry(2.1298037437129635) qpb[4];
ry(1.9796547215466507) qpb[5];
ry(0.9528520923152316) qpb[6];
ry(2.0577065163938895) qpb[7];
crz(0.2205) qpb[0], qpb[1];
crz(0.2205) qpb[1], qpb[0];
crz(-0.31949999999999995) qpb[1], qpb[2];
crz(-0.31949999999999995) qpb[2], qpb[1];
crz(0.17099999999999999) qpb[2], qpb[3];
crz(0.17099999999999999) qpb[3], qpb[2];
crz(-0.12375) qpb[3], qpb[4];
crz(-0.12375) qpb[4], qpb[3];
crz(0.25425000000000003) qpb[4], qpb[5];
crz(0.25425000000000003) qpb[5], qpb[4];
crz(0.20024999999999998) qpb[5], qpb[6];
crz(0.20024999999999998) qpb[6], qpb[5];
crz(-0.15075) qpb[6], qpb[7];
crz(-0.15075) qpb[7], qpb[6];
crz(0.11025) qpb[0], qpb[2];
crz(0.11025) qpb[2], qpb[0];
crz(-0.15974999999999998) qpb[1], qpb[3];
crz(-0.15974999999999998) qpb[3], qpb[1];
crz(0.08549999999999999) qpb[2], qpb[4];
crz(0.08549999999999999) qpb[4], qpb[2];
crz(-0.061875) qpb[3], qpb[5];
crz(-0.061875) qpb[5], qpb[3];
crz(0.12712500000000002) qpb[4], qpb[6];
crz(0.12712500000000002) qpb[6], qpb[4];
crz(0.10012499999999999) qpb[5], qpb[7];
crz(0.10012499999999999) qpb[7], qpb[5];
crz(0.055125) qpb[0], qpb[3];
crz(0.055125) qpb[3], qpb[0];
crz(-0.07987499999999999) qpb[1], qpb[4];
crz(-0.07987499999999999) qpb[4], qpb[1];
crz(0.042749999999999996) qpb[2], qpb[5];
crz(0.042749999999999996) qpb[5], qpb[2];
crz(-0.0309375) qpb[3], qpb[6];
crz(-0.0309375) qpb[6], qpb[3];
crz(0.06356250000000001) qpb[4], qpb[7];
crz(0.06356250000000001) qpb[7], qpb[4];
rz(-2.042035224833365) qpb[0];
rz(2.042035224833365) qpb[1];
rz(-2.042035224833365) qpb[2];
rz(-2.042035224833365) qpb[3];
rz(2.042035224833365) qpb[4];
rz(2.042035224833365) qpb[5];
rz(-2.042035224833365) qpb[6];
rz(2.042035224833365) qpb[7];
ry(1.2033550686281267) qpb[0];
ry(2.1595100671007774) qpb[1];
ry(1.47096257800141) qpb[2];
ry(0.6272479147849687) qpb[3];
ry(2.723304167019916) qpb[4];
ry(2.5824719581736915) qpb[5];
ry(0.36996352537200744) qpb[6];
ry(2.658975174669196) qpb[7];
crz(0.392) qpb[0], qpb[1];
crz(0.392) qpb[1], qpb[0];
crz(-0.568) qpb[1], qpb[2];
crz(-0.568) qpb[2], qpb[1];
crz(0.304) qpb[2], qpb[3];
crz(0.304) qpb[3], qpb[2];
crz(-0.22) qpb[3], qpb[4];
crz(-0.22) qpb[4], qpb[3];
crz(0.452) qpb[4], qpb[5];
crz(0.452) qpb[5], qpb[4];
crz(0.356) qpb[5], qpb[6];
crz(0.356) qpb[6], qpb[5];
crz(-0.268) qpb[6], qpb[7];
crz(-0.268) qpb[7], qpb[6];
crz(0.196) qpb[0], qpb[2];
crz(0.196) qpb[2], qpb[0];
crz(-0.284) qpb[1], qpb[3];
crz(-0.284) qpb[3], qpb[1];
crz(0.152) qpb[2], qpb[4];
crz(0.152) qpb[4], qpb[2];
crz(-0.11) qpb[3], qpb[5];
crz(-0.11) qpb[5], qpb[3];
crz(0.226) qpb[4], qpb[6];
crz(0.226) qpb[6], qpb[4];
crz(0.178) qpb[5], qpb[7];
crz(0.178) qpb[7], qpb[5];
crz(0.098) qpb[0], qpb[3];
crz(0.098) qpb[3], qpb[0];
crz(-0.142) qpb[1], qpb[4];
crz(-0.142) qpb[4], qpb[1];
crz(0.076) qpb[2], qpb[5];
crz(0.076) qpb[5], qpb[2];
crz(-0.055) qpb[3], qpb[6];
crz(-0.055) qpb[6], qpb[3];
crz(0.113) qpb[4], qpb[7];
crz(0.113) qpb[7], qpb[4];
rz(-pi) qpb[0];
rz(pi) qpb[1];
rz(-pi) qpb[2];
rz(-pi) qpb[3];
rz(pi) qpb[4];
rz(pi) qpb[5];
rz(-pi) qpb[6];
rz(pi) qpb[7];
wc[0] = measure qpb[0];
wc[1] = measure qpb[1];
wc[2] = measure qpb[2];
wc[3] = measure qpb[3];
wc[4] = measure qpb[4];
wc[5] = measure qpb[5];
wc[6] = measure qpb[6];
wc[7] = measure qpb[7];
