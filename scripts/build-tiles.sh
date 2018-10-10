#!/usr/bin/env bash

for D in ./data/*; do
    if [ -d "${D}" ]; then
        trueColorFile="${D}/true_color.tif"
        trueColorOutputPath="${D}/tiles"
        ndviFile="${D}/ndvi.tif"
        ndviOutputPath="${D}/ndvi_tiles"

        gdal2tiles.py -p mercator -z 1-15 "${trueColorFile}" "${trueColorOutputPath}"

        python common/ndvi.py "${D}" "${ndviFile}"
        gdal2tiles.py -p mercator -z 1-15 "${ndviFile}" "${ndviOutputPath}"
    fi
done

tree ./data