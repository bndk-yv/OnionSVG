from onion_svg import SplitSVG

svg = SplitSVG('example.svg')
svg.save_all('output', dpi = 200)