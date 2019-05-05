from OnionSVG.__init__ import OnionSVG, check_svg

svg = OnionSVG('example')

# svg.peel("output/all", dpi = 100)
svg.peel("Layer [0-2]", to = "output", dpi = 200)
