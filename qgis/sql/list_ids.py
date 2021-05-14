layer = qgis.utils.iface.activeLayer()
selected_features = layer.selectedFeatures()
id_list = []
for i in selected_features:
    tmp = i.attribute("adm1_code")
    id_list.append(tmp)
print(id_list)