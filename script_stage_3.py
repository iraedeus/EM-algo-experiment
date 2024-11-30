from pathlib import Path

from experimental_env.analysis.analysis import Analysis
from experimental_env.analysis.analyze_strategies.density_plot import DensityPlot
from experimental_env.analysis.analyze_strategies.error_convergence import (
    ErrorConvergence,
)
from experimental_env.analysis.analyze_strategies.time_plot import TimePlot
from experimental_env.analysis.metrics import MSE, Parametric
from experimental_env.experiment.experiment_parser import ExperimentParser

EXPERIMENT_DIR = "experiment"
WORKING_DIR = Path(
    f"/home/danil/PycharmProjects/Projects/EM-algo-DT/{EXPERIMENT_DIR}/stage_3"
)


# Compare results
LMOMENTS_DIR = Path(
    f"/home/danil/PycharmProjects/Projects/EM-algo-DT/{EXPERIMENT_DIR}/stage_2/LMoments"
)
LIKELIHOOD_DIR = Path(
    f"/home/danil/PycharmProjects/Projects/EM-algo-DT/{EXPERIMENT_DIR}/stage_2/Likelihood"
)

results_1 = ExperimentParser().parse(LMOMENTS_DIR)
results_2 = ExperimentParser().parse(LIKELIHOOD_DIR)

analyze_actions = [DensityPlot(), TimePlot(), ErrorConvergence(MSE())]


Analysis(WORKING_DIR, analyze_actions).analyze(results_1, "LMoments")
Analysis(WORKING_DIR, analyze_actions).analyze(results_2, "Likelihood")
Analysis(WORKING_DIR, analyze_actions).compare(
    results_1, results_2, "LMoments", "Likelihood"
)
