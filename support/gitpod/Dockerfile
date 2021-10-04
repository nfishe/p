FROM gitpod/workspace-base:latest

ARG MAMBAFORGE_VERSION="4.10.0-0"
ARG CONDA_ENV=plo-dev


# ---- Configure environment ----
ENV CONDA_DIR=/home/gitpod/mambaforge3 \
    SHELL=/bin/bash
ENV PATH=${CONDA_DIR}/bin:$PATH \
    WORKSPACE=/workspace/plo

USER root

# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
    ca-certificates \
    dirmngr \
    dvisvgm \
    gnupg \
    gpg-agent \
    texlive-latex-extra \
    vim && \
    # this needs to be done after installing dirmngr
    apt-key adv --keyserver keyserver.ubuntu.com --recv-key C99B11DEB97541F0 && \
    apt-add-repository https://cli.github.com/packages && \
    apt-get install -yq --no-install-recommends \
    gh && \
    locale-gen en_US.UTF-8 && \
    apt-get clean && \
    rm -rf /var/cache/apt/* &&\
    rm -rf /var/lib/apt/lists/* &&\
    rm -rf /tmp/*

# Allows this Dockerfile to activate conda environments
SHELL ["/bin/bash", "--login", "-o", "pipefail", "-c"]

RUN wget -q -O mambaforge3.sh \
    "https://github.com/conda-forge/miniforge/releases/download/$MAMBAFORGE_VERSION/Mambaforge-$MAMBAFORGE_VERSION-Linux-x86_64.sh" && \
    bash mambaforge3.sh -p ${CONDA_DIR} -b && \
    rm mambaforge3.sh

COPY environment.yml /tmp/environment.yml

# -----------------------------------------------------------------------------
# ---- Create conda environment ----
# Install NumPy dependencies
RUN mamba env create -f /tmp/environment.yml && \
    conda activate ${CONDA_ENV} && \
    mamba install ccache -y && \
    # needed for docs rendering later on
    python -m pip install --no-cache-dir sphinx-autobuild && \
    conda clean --all -f -y && \
    rm -rf /tmp/*

# -----------------------------------------------------------------------------
# Always make sure we are not root
USER gitpod