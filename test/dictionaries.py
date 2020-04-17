from factiva.core import dicts

cl = dicts.countries_list()
assert cl.shape[0] == 250
assert cl.shape[1] == 19

rh = dicts.regions_hierarchy()
assert rh.shape[0] == 299
assert rh.shape[1] == 4

ih = dicts.industries_hierarchy()
assert ih.shape[0] == 986
assert ih.shape[1] == 3
