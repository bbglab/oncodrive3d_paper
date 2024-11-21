# Paths
# -----

SUBDIR = "human_mane_raw"
RUN = "run_2024-07-01_16-04-14"

SUBDIR_CH = "run_20241004_ch"
RUN_CH = "run_2024-11-04_13-09-49"

RUN_MOUSE = "run_2024-11-19_23-08-05"


# Names and colors
# ----------------

colors_dict = {"Oncodrive3D" : "#ffad48", 
              "HotMAPS" : "#024b79", 
              "OncodriveCLUSTL" : "#43b7c2", 
              "smRegions" : "#c2f1ce", 
              "CBaSE" : "#ffb8b3", 
              "SEISMIC" : "#ede5ff", 
              "dNdScv" : "#edd7c5", 
              "MutPanning" : "#cee4d8", 
              "OncodriveFML" : "#bbd9f6",
              "IntOGen" : "#A6D854",
              "OncoKB" : "#66C2A5",
              "CGC" : "#FFA04D",
              "MSK-IMPACT" : "#FB9A99",
              "MSK-IMPACT Heme" : "#E31A1C",
              "FoundationOne" : "#CAB2D6",
              "FoundationOne Heme" : "#6A3D9A",
              "Vogelstein" : "#E5C494",

              "IntOGen CH" : "#ff4d4d",
              "IntOGen AML" : "#f3588e",
              "IntOGen others" : "#A6D854",
              "IntOGen Cancer" : "#A6D854",
               
              "CGC AML" : "#FFA04D",
              "CGC others" : "#FFA04D"}

names_dict = {"o3d" : "Oncodrive3D", 
             "hotmaps" : "HotMAPS", 
             "clustl" : "OncodriveCLUSTL", 
             "smreg" : "smRegions", 
             "cbase" : "CBaSE", 
             "seismic" : "SEISMIC", 
             "dndscv" : "dNdScv", 
             "mutpan" : "MutPanning", 
             "fml" : "OncodriveFML",
             "intogen" : "IntOGen",
             "oncokb" : "OncoKB",
             "cgc" : "CGC",
             "msk_impact" : "MSK-IMPACT",
             "msk_heme" : "MSK-IMPACT Heme",
             "fondone" : "FoundationOne",
             "fondone_heme" : "FoundationOne Heme", 
             "vogelstein" : "Vogelstein",

             "intogen" : "IntOGen Cancer",
             "intogen_ch" : "IntOGen CH",
             "intogen_aml" : "IntOGen AML",
             "intogen_others" : "IntOGen others",
              
             "CGC_specific" : "CGC AML",
             "CGC_not_specific" : "CGC others"}

annot_cols = ["Gene", 
              "cgc", 
              "intogen", 
              "hotmaps", 
              "clustl", 
              "smreg", 
              "cbase",
              "dndscv", 
              "mutpan", 
              "fml",

              "intogen_ch",
              "intogen_aml",
              "intogen_others",
              
              "CGC_specific",
              "CGC_not_specific"]