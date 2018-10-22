from onion_svg import OnionSVG

svg = OnionSVG('example')

# svg.peel('all', dpi = 100)
svg.peel("Layer [0-2]", to = "re", dpi = 200)
