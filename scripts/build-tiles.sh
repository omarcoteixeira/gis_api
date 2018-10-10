#!/usr/bin/env bash

for D in ./data/*; do
    if [ -d "${D}" ]; then
        trueColorFile="${D}/true_color.tif"
        outputPath="${D}/tiles"

        gdal2tiles.py --profile=mercator --zoom=11-15 "${trueColorFile}" "${outputPath}"
    fi
done