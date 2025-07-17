import matplotlib.pyplot as plt
from qldpc.codes import HGPCode, ClassicalCode
from utils import make_error_rate_figure
from Graph import generate_biregular_bipartite_graph
import numpy as np

# Hypergraph product codes created with random (3,4)-regular bipartite graphs.
G1 = generate_biregular_bipartite_graph(4,3,3,4)
classical_code1 = ClassicalCode(G1)
hgpc1 = HGPCode(classical_code1, classical_code1)

G2 = generate_biregular_bipartite_graph(12,9,3,4)
classical_code2 = ClassicalCode(G2)
hgpc2 = HGPCode(classical_code2, classical_code2)

G3 = generate_biregular_bipartite_graph(20,15,3,4)
classical_code3 = ClassicalCode(G3)
hgpc3 = HGPCode(classical_code3, classical_code3)

G4 = generate_biregular_bipartite_graph(28,21,3,4)
classical_code4 = ClassicalCode(G4)
hgpc4 = HGPCode(classical_code4, classical_code4)

codes = [hgpc1, hgpc2, hgpc3, hgpc4]

make_error_rate_figure(codes, physical_rates= np.logspace(-3,-0.01,100), num_samples=100, with_BP_OSD=True, distance_estimation_trials=100)
plt.show()