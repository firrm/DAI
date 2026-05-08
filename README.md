# Data & AI in Economics 

Welcome to [our](https://www.finance.wiwi.tu-dortmund.de) lecture repo for the course "Data & AI in Economics" at the [TU Dortmund University](https://www.tu-dortmund.de). 

# Links
[Lectures](lectures.md)

[Literature](literature.md)

[Missions](missions.md)

[Datasets](datasets.md)

[Timetable](https://moodle.tu-dortmund.de)

# Setup
As a student you are elegible to use the Github Student program including Copilot, I suggest you sign up for it [here](https://education.github.com/benefits?type=student).


# Quick start with Docker (recommended)

The easiest way to run all notebooks locally — no Python installation or cloning required.

**Prerequisites:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows / macOS / Linux).

```bash
# 1. Download the compose file (one-time)
curl -O https://raw.githubusercontent.com/firrm/DAI/main/docker-compose.yml

# 2. Start JupyterLab (pulls the image automatically on first run)
docker compose up
```

Then open **http://localhost:8888** in your browser.

All course materials (lectures, exercises, data) are available inside the notebook file browser.
Your own files saved in the **`work/`** folder persist between sessions via the `./my-work` volume on your machine.

> **Note:** The deep-learning notebooks `05a_deep_learning` and `05b_deep_learning` require
> TensorFlow/Keras and will not run in this image. Use the local setup below for those.

# Local environment setup (optional)
Since we will put everything on our server, you will **not** need to do this. However, if you want to work on your local machine, you will need to do the following:

## How to use Git
Git is a version control system that allows you to track changes in your code. It is a very powerful tool that is widely used in the industry. We will use it in this course to manage the code and the data.
'git' is a command line tool. You can use it in the terminal or in the command prompt. If you are not familiar with the command line, you can use a graphical user interface (GUI) for git. There are many GUIs available, but we recommend [GitHub Desktop](https://desktop.github.com/).

### Install Git
To install git, follow the instructions on the [official website](https://git-scm.com/).

### Clone the repository
To clone the repository, open the terminal or the command prompt and navigate to the directory where you want to store the repository. Then run the following command:

```bash
git clone https://github.com/firrm/DAI.git
```

## How to use Python 
We will use Python as the programming language for this course. Python is a very popular language for data analysis and machine learning. It has a large and active community, and there are many libraries available for data analysis, visualization, and machine learning.

### Install Python
To install Python, follow the instructions on the [official website](https://www.python.org/).

## How to use UV
We will use UV to manage the dependencies of the project. UV is a tool for dependency management and packaging in Python. It allows you to declare the dependencies of your project in a simple and declarative way, and it will automatically install the dependencies for you.
Why? Because it is 10-100x faster than pip and includes all the tools you need to manage your Python project.

### Install UV
To install UV, follow the instructions of your local OS

### Install the dependencies
To install the dependencies of the project, run the following command in the terminal or the command prompt:

```bash
uv sync
```
### From uv to pip
If you want to use pip instead of poetry, you can run the following command in the terminal or the command prompt:

```bash
uv export --output-file requirements.txt
uv pip install -r requirements.txt
```

## How to use Jupyter Notebooks
We will use Jupyter Notebooks to write the code. Jupyter Notebooks are a great tool for data analysis and visualization. They allow you to write and execute code, view the results, and add text and images. You can also export the notebooks to different formats, such as HTML, PDF, or slides.

### Install Jupyter Notebook
To install Jupyter Notebook, follow the instructions on the [official website](https://jupyter.org/).
