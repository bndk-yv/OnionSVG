from onionsvg import OnionSVG

svg = OnionSVG('example')

# svg.peel("output/all", dpi = 100)
svg.peel("Layer [0-2]", to = "output/re", dpi = 200)
