from setuptools import setup, find_packages

setup(
    name="lm-nav",
    version="1.0",
    description="Source code for the LMNav.",
    author="Błażej Osiński & Dhruv Shah",
    packages=['lm_nav'],
    install_requires=[
        "networkx==2.6.3",
        "h5py==3.7.0",
        "matplotlib==3.5.2",
        "numpy>=1.23.0",  # ✅ Fixed NumPy version for Python 3.11+
        "pillow",
        "pyyaml",
        "utm==0.7.0",
        "openai==0.20.0",
        "jupyter==1.0.0",
        "opencv-python==4.6.0.66",
        "torch",  # ✅ Removed fixed version to allow latest compatible
        "torchaudio",
        "torchvision",
        "ftfy==6.1.1",
        "regex==2022.6.2",
        "tqdm==4.64.0",
        "clip @ git+https://github.com/openai/CLIP.git",
        "spacy>=3.5.0",  # ✅ Updated spaCy for Python 3.11 compatibility
        "gdown==4.5.1",
    ],
    package_data={'': ['base.css.html', 'bgraph.js']},
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)

