#!/usr/bin/env bash

# Clone submodules recursively
git submodule update --init --recursive

MODEL=large-v3

./whisper.cpp/models/download-ggml-model.sh $MODEL

echo "Generating CoreML model..."

if [ -f "whisper.cpp/models/coreml-encoder-${MODEL}.mlmodelc/coremldata.bin" ]; then
    echo "CoreML model already exists. Skipping generation."
else
    ./whisper.cpp/models/generate-coreml-model.sh $MODEL
fi

echo "Compile whisper.cpp"

cd whisper.cpp || exit

WHISPER_COREML=1 make -j