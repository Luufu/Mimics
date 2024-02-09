


# Open the project
#input_dir = r'C:\MedData\Files\Mimi.mcs'
#mimics.file.open_project(input_dir)
#Empty Mask     
mask_a = mimics.segment.create_mask()
mask_a.name = "Bone"
mimics.segment.threshold(mask=mask_a, threshold_min=1250, threshold_max=2800) 
point_1 = mimics.analyze.indicate_point(title="Region growing point", message = "Please indicate a point on the part of interest")
mask_a.visible = False
point_2 = point_1.coordinates
point_2 = tuple(point_2)
mask_b = mimics.segment.region_grow(point=point_2, input_mask=mask_a, target_mask=None, slice_type="Axial", keep_original_mask=True)
mask_b.name = "Segmented bone"
mask_c = mimics.segment.activate_multiple_slice_edit(
    mask= mask_b,
    operation="Remove",
    edit_type="Ellipse",
    edit_mode="Draw",
    hide_markings=False,
    enable_auto_interpolate=False)
#point_3 = mimics.analyze.indicate_point(title="Region growing point", message="Please indicate a point on the part of interest")
#mask_c = mimics.segment.region_grow(point=point_3, input_mask= mask_b, target_mask = None, slice_type = "Axial", keep_original_mask=True)
mask_c.name = "Right Hemi-Pelvis"
mimics.segment.split_mask(selection=mask_b , regions = mask_c )
mask_b.visible = False
#mask_d = mimics.segment.boolean_operations(mask_b = mimics.data.find("Segmented Bone"), mask_c = mimics.data.find("Right Hemi-Pelvis") )




mimics.segment.split_mask(mask = mask_b, )

while i <= 5:
    point_3 = mimics.analyze.indicate_point(title="Split mask point", message = "Please indicate a point on the part of interest")
    mimics.segment.split_mask



# Export the STL
#mimics.file.export_part(object_to_convert=part_a, file_name=r"C:\MedData\skull_of_Mimi.stl")
# Save the project
#mimics.file.save_project()