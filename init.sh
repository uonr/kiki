#!/usr/bin/env bash

MODEL=medium

./whisper.cpp/models/download-ggml-model.sh $MODEL

echo "Generating CoreML model..."

./whisper.cpp/models/generate-coreml-model.sh $MODEL
