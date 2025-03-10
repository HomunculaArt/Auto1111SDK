from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.95'
DESCRIPTION = 'SDK for Automatic 1111.'
LONG_DESCRIPTION = 'A package that allows you to easily generate images and run diffusion models the same way as Automatic 1111.'

# Setting up
setup(
    name="auto1111sdk",
    version=VERSION,
    author="Auto1111 SDK",
    author_email="saketh.kotamraju@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    "GitPython",
    "Pillow",
    "accelerate",
    "basicsr",
    "blendmodes",
    "clean-fid",
    "einops",
    "fastapi",
    "gfpgan",
    "gradio",
    "httpcore",
    "inflection",
    "jsonmerge",
    "kornia",
    "lark",
    "numpy",
    "omegaconf",
    "open-clip-torch",
    "piexif",
    "psutil",
    "pytorch_lightning",
    "realesrgan",
    "resize-right",
    "safetensors",
    "scikit-image",
    "timm",
    "tomesd",
    "torch",
    "torchdiffeq",
    "torchsde",
    "transformers",
    "httpx",
    "clip"
],
    keywords=['python', 'Automatic 1111', 'Stable Diffusion Web UI', 'image generation', 'stable diffusion', 'civit ai'], 
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
