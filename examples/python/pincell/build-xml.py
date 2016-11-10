import openmc

###############################################################################
#                      Simulation Input File Parameters
###############################################################################

# OpenMC simulation parameters
batches = 100
inactive = 10
particles = 1000


###############################################################################
#                 Exporting to OpenMC materials.xml file
###############################################################################

# Instantiate some Nuclides
h1 = openmc.Nuclide('H1')
h2 = openmc.Nuclide('H2')
he4 = openmc.Nuclide('He4')
b10 = openmc.Nuclide('B10')
b11 = openmc.Nuclide('B11')
o16 = openmc.Nuclide('O16')
o17 = openmc.Nuclide('O17')
cr50 = openmc.Nuclide('Cr50')
cr52 = openmc.Nuclide('Cr52')
cr53 = openmc.Nuclide('Cr53')
cr54 = openmc.Nuclide('Cr54')
fe54 = openmc.Nuclide('Fe54')
fe56 = openmc.Nuclide('Fe56')
fe57 = openmc.Nuclide('Fe57')
fe58 = openmc.Nuclide('Fe58')
zr90 = openmc.Nuclide('Zr90')
zr91 = openmc.Nuclide('Zr91')
zr92 = openmc.Nuclide('Zr92')
zr94 = openmc.Nuclide('Zr94')
zr96 = openmc.Nuclide('Zr96')
sn112 = openmc.Nuclide('Sn112')
sn114 = openmc.Nuclide('Sn114')
sn115 = openmc.Nuclide('Sn115')
sn116 = openmc.Nuclide('Sn116')
sn117 = openmc.Nuclide('Sn117')
sn118 = openmc.Nuclide('Sn118')
sn119 = openmc.Nuclide('Sn119')
sn120 = openmc.Nuclide('Sn120')
sn122 = openmc.Nuclide('Sn122')
sn124 = openmc.Nuclide('Sn124')
u = openmc.Element('U')
o = openmc.Element('O')

# Instantiate some Materials and register the appropriate Nuclides
uo2 = openmc.Material(material_id=1, name='UO2 fuel at 2.4% wt enrichment')
uo2.set_density('g/cm3', 10.29769)
uo2.add_element(u, 1., enrichment=2.4)
uo2.add_element(o, 2.)

helium = openmc.Material(material_id=2, name='Helium for gap')
helium.set_density('g/cm3', 0.001598)
helium.add_nuclide(he4, 2.4044e-4)

zircaloy = openmc.Material(material_id=3, name='Zircaloy 4')
zircaloy.set_density('g/cm3', 6.55)
zircaloy.add_nuclide(o16, 3.0743e-4)
zircaloy.add_nuclide(o17, 7.4887e-7)
zircaloy.add_nuclide(cr50, 3.2962e-6)
zircaloy.add_nuclide(cr52, 6.3564e-5)
zircaloy.add_nuclide(cr53, 7.2076e-6)
zircaloy.add_nuclide(cr54, 1.7941e-6)
zircaloy.add_nuclide(fe54, 8.6699e-6)
zircaloy.add_nuclide(fe56, 1.3610e-4)
zircaloy.add_nuclide(fe57, 3.1431e-6)
zircaloy.add_nuclide(fe58, 4.1829e-7)
zircaloy.add_nuclide(zr90, 2.1827e-2)
zircaloy.add_nuclide(zr91, 4.7600e-3)
zircaloy.add_nuclide(zr92, 7.2758e-3)
zircaloy.add_nuclide(zr94, 7.3734e-3)
zircaloy.add_nuclide(zr96, 1.1879e-3)
zircaloy.add_nuclide(sn112, 4.6735e-6)
zircaloy.add_nuclide(sn114, 3.1799e-6)
zircaloy.add_nuclide(sn115, 1.6381e-6)
zircaloy.add_nuclide(sn116, 7.0055e-5)
zircaloy.add_nuclide(sn117, 3.7003e-5)
zircaloy.add_nuclide(sn118, 1.1669e-4)
zircaloy.add_nuclide(sn119, 4.1387e-5)
zircaloy.add_nuclide(sn120, 1.5697e-4)
zircaloy.add_nuclide(sn122, 2.2308e-5)
zircaloy.add_nuclide(sn124, 2.7897e-5)

borated_water = openmc.Material(material_id=4, name='Borated water at 975 ppm')
borated_water.set_density('g/cm3', 0.740582)
borated_water.add_nuclide(b10, 8.0042e-6)
borated_water.add_nuclide(b11, 3.2218e-5)
borated_water.add_nuclide(h1, 4.9457e-2)
borated_water.add_nuclide(h2, 7.4196e-6)
borated_water.add_nuclide(o16, 2.4672e-2)
borated_water.add_nuclide(o17, 6.0099e-5)
borated_water.add_s_alpha_beta('c_H_in_H2O')

# Instantiate a Materials collection and export to XML
materials_file = openmc.Materials([uo2, helium, zircaloy, borated_water])
materials_file.export_to_xml()


###############################################################################
#                 Exporting to OpenMC geometry.xml file
###############################################################################

# Instantiate ZCylinder surfaces
fuel_or = openmc.ZCylinder(surface_id=1, x0=0, y0=0, R=0.39218, name='Fuel OR')
clad_ir = openmc.ZCylinder(surface_id=2, x0=0, y0=0, R=0.40005, name='Clad IR')
clad_or = openmc.ZCylinder(surface_id=3, x0=0, y0=0, R=0.45720, name='Clad OR')
left = openmc.XPlane(surface_id=4, x0=-0.62992, name='left')
right = openmc.XPlane(surface_id=5, x0=0.62992, name='right')
bottom = openmc.YPlane(surface_id=6, y0=-0.62992, name='bottom')
top = openmc.YPlane(surface_id=7, y0=0.62992, name='top')

left.boundary_type = 'reflective'
right.boundary_type = 'reflective'
top.boundary_type = 'reflective'
bottom.boundary_type = 'reflective'

# Instantiate Cells
fuel = openmc.Cell(cell_id=1, name='cell 1')
gap = openmc.Cell(cell_id=2, name='cell 2')
clad = openmc.Cell(cell_id=3, name='cell 3')
water = openmc.Cell(cell_id=4, name='cell 4')

# Use surface half-spaces to define regions
fuel.region = -fuel_or
gap.region = +fuel_or & -clad_ir
clad.region = +clad_ir & -clad_or
water.region = +clad_or & +left & -right & +bottom & -top

# Register Materials with Cells
fuel.fill = uo2
gap.fill = helium
clad.fill = zircaloy
water.fill = borated_water

# Instantiate Universe
root = openmc.Universe(universe_id=0, name='root universe')

# Register Cells with Universe
root.add_cells([fuel, gap, clad, water])

# Instantiate a Geometry, register the root Universe, and export to XML
geometry = openmc.Geometry(root)
geometry.export_to_xml()


###############################################################################
#                   Exporting to OpenMC settings.xml file
###############################################################################

# Instantiate a Settings object, set all runtime parameters, and export to XML
settings_file = openmc.Settings()
settings_file.batches = batches
settings_file.inactive = inactive
settings_file.particles = particles

# Create an initial uniform spatial source distribution over fissionable zones
bounds = [-0.62992, -0.62992, -1, 0.62992, 0.62992, 1]
uniform_dist = openmc.stats.Box(bounds[:3], bounds[3:], only_fissionable=True)
settings_file.source = openmc.source.Source(space=uniform_dist)

settings_file.entropy_lower_left = [-0.39218, -0.39218, -1.e50]
settings_file.entropy_upper_right = [0.39218, 0.39218, 1.e50]
settings_file.entropy_dimension = [10, 10, 1]
settings_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC tallies.xml file
###############################################################################

# Instantiate a tally mesh
mesh = openmc.Mesh(mesh_id=1)
mesh.type = 'regular'
mesh.dimension = [100, 100, 1]
mesh.lower_left = [-0.62992, -0.62992, -1.e50]
mesh.upper_right = [0.62992, 0.62992, 1.e50]

# Instantiate some tally Filters
energy_filter = openmc.EnergyFilter([0., 4., 20.e6])
mesh_filter = openmc.MeshFilter(mesh)

# Instantiate the Tally
tally = openmc.Tally(tally_id=1, name='tally 1')
tally.filters = [energy_filter, mesh_filter]
tally.scores = ['flux', 'fission', 'nu-fission']

# Instantiate a Tallies collection and export to XML
tallies_file = openmc.Tallies([tally])
tallies_file.export_to_xml()
