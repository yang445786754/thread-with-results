import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thread_with_results", 
    version="1.0.1",
    author="Tony_9410",
    author_email="tony_9410@foxmail.com",
    description="Python thread with results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yang445786754/thread-with-results",
    project_urls={
        'Homepage': 'https://github.com/yang445786754/thread-with-results',
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    setup_requires=['wheel'],
)
