from pathlib import Path

from experimental_env.preparation.dataset_generator import (
    ConcreteDatasetGenerator,
    RandomDatasetGenerator,
)
from mpest.models import ExponentialModel, GaussianModel, WeibullModelExp

WORKING_DIR = Path("/home/danil/PycharmProjects/Projects/EM-algo-DT/experiment/stage_1")
SAMPLES_SIZE = 200

r_generator = RandomDatasetGenerator(42)
mixtures = [
    [ExponentialModel],
    [GaussianModel],
    [WeibullModelExp],
    [WeibullModelExp, GaussianModel],
    [ExponentialModel, GaussianModel],
    [WeibullModelExp, WeibullModelExp],
]
for models in mixtures:
    r_generator.generate(SAMPLES_SIZE, models, Path(WORKING_DIR), exp_count=100)

c_generator = ConcreteDatasetGenerator(42)
models = [GaussianModel, WeibullModelExp]
c_generator.add_distribution(models[0], [0, 1.0], 0.5)
c_generator.add_distribution(models[1], [1, 1], 0.5)
c_generator.generate(SAMPLES_SIZE, Path(WORKING_DIR), 5)

c_generator2 = ConcreteDatasetGenerator(42)
models = [ExponentialModel]
c_generator2.add_distribution(models[0], [1.0], 1.0)
c_generator2.generate(SAMPLES_SIZE, Path(WORKING_DIR), 5)

c_generator3 = ConcreteDatasetGenerator(42)
models = [GaussianModel]
c_generator3.add_distribution(models[0], [0, 1.0], 1.0)
c_generator3.generate(SAMPLES_SIZE, Path(WORKING_DIR), 5)

c_generator4 = ConcreteDatasetGenerator(42)
models = [WeibullModelExp]
c_generator4.add_distribution(models[0], [1.0, 1.0], 1.0)
c_generator4.generate(SAMPLES_SIZE, Path(WORKING_DIR), 5)

c_generator5 = ConcreteDatasetGenerator(42)
models = [WeibullModelExp]
c_generator5.add_distribution(models[0], [1.0, 1.0], 1.0)
c_generator5.generate(SAMPLES_SIZE, Path(WORKING_DIR), 5)

c_generator6 = ConcreteDatasetGenerator(42)
models = [WeibullModelExp]
c_generator6.add_distribution(models[0], [1.0, 0.5], 1.0)
c_generator6.generate(SAMPLES_SIZE, Path(WORKING_DIR), 5)

c_generator7 = ConcreteDatasetGenerator(42)
models = [GaussianModel, GaussianModel]
c_generator7.add_distribution(models[0], [-1.0, 2.5], 0.3)
c_generator7.add_distribution(models[1], [1.0, 0.5], 0.7)
c_generator7.generate(SAMPLES_SIZE, Path(WORKING_DIR), 5)
