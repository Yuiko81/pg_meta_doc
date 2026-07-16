# PostgreSQL Schema Report

- Generated at: `2026-07-16T07:38:55.114293+00:00`
- Source: `postgresql+psycopg://mon1:***@192.168.11.181:5432/mon1db`
- Tables: `207`
- Issues: `272`

## ERD

```mermaid
graph LR
  year_2018_T_Cell_ReadOnly["year_2018.T_Cell_ReadOnly\nID\nID_Form\nID_Section\nID_Col\nID_Row\n..."]
  year_2018_T_Cell_ReadOnly_MON["year_2018.T_Cell_ReadOnly_MON\nID\nID_Form\nID_Section\nID_Col\nID_Row\n..."]
  year_2018_T_DATA["year_2018.T_DATA\nRec (PK)\nID\nID_Form\nID_Vo\nID_Section\n..."]
  year_2018_T_DIC_GROUP_INST["year_2018.T_DIC_GROUP_INST\nID_DIC\nKOD\nNAME\nKOD_NAME\nSelected"]
  year_2018_T_DIC_NAUKA["year_2018.T_DIC_NAUKA\nID_DIC (PK)\nKOD\nNAME\nKod_Kval\nKOD_NAME\n..."]
  year_2018_T_DIC_REPUBLIC["year_2018.T_DIC_REPUBLIC\nID_DIC\nKOD (PK)\nID_Type\nName\nKOD_NAME\n..."]
  year_2018_T_DIC_SPEC["year_2018.T_DIC_SPEC\nID_DIC (PK)\nKOD\nKod_Kval\nNAME\nKOD_NAME\n..."]
  year_2018_T_DIC_SPECIFIC["year_2018.T_DIC_SPECIFIC\nID_DIC\nKOD\nNAME\nNAME_F"]
  year_2018_T_DIC_SPEC_CLOSED["year_2018.T_DIC_SPEC_CLOSED\nID_DIC"]
  year_2018_T_DIC_SPEC_SPECIFIC["year_2018.T_DIC_SPEC_SPECIFIC\nID_DIC\nKOD\nKod_Kval\nNAME\nKOD_NAME\n..."]
  year_2018_T_DIC_UGS["year_2018.T_DIC_UGS\nID_DIC\nKOD\nNAME\nID_OTRASL"]
  year_2018_T_ERROR["year_2018.T_ERROR\nID\nForm_ID\nVO_ID\nSection_ID\nSTRK\n..."]
  year_2018_T_FO["year_2018.T_FO\nNFO (PK)\nNAME"]
  year_2018_T_Form_Cell["year_2018.T_Form_Cell\nID\nID_Col\nID_Row\nDic_Source\nFormat_Cell\n..."]
  year_2018_T_Form_Col["year_2018.T_Form_Col\nID\nID_Form\nID_Section\nID_Column_Num\nID_Type_Col\n..."]
  year_2018_T_Form_Col_Appendix["year_2018.T_Form_Col_Appendix\nID\nID_Form\nID_Section\nID_Column_Num\nID_Type_Col\n..."]
  year_2018_T_Form_Col_SumTotal["year_2018.T_Form_Col_SumTotal\nID\nID_FORM\nID_SECTION\nID_COL_NUM_DEST\nID_COL_NUM_CURRENT\n..."]
  year_2018_T_Form_Register["year_2018.T_Form_Register\nID\nID_Form\nID_Inst\nID_User\nForm_Status\n..."]
  year_2018_T_Form_Row["year_2018.T_Form_Row\nID (PK)\nID_FORM\nID_SECTION\nSECTION_TYPE\nID_ROW_NUM\n..."]
  year_2018_T_Form_Row_SumTotal["year_2018.T_Form_Row_SumTotal\nID\nID_FORM\nID_SECTION\nID_ROW_NUM_TOTAL\nID_ROW_NUM_SUM\n..."]
  year_2018_T_Form_SumTotal["year_2018.T_Form_SumTotal\nID\nID_FORM\nID_SECTION\nID_ROW_TOTAL\nID_COL_NUM_DEST\n..."]
  year_2018_T_Forms["year_2018.T_Forms\nID\nOKUD\nName\nShort_Name\nData_Start\n..."]
  year_2018_T_INSTITUTION["year_2018.T_INSTITUTION\nID (PK)\nParent_ID\npzk\nName\nter\n..."]
  year_2018_T_LIST_FIL["year_2018.T_LIST_FIL\nREC\nID\nName\nTYPE\nOKATO\n..."]
  year_2018_T_LIST_UCH["year_2018.T_LIST_UCH\nREC\nID\nName\nPOST\nKOD_TEL\n..."]
  year_2018_T_OU_SPECIFIC["year_2018.T_OU_SPECIFIC\nID_OU\nNAME_OU\nKOD_SPECIFIC\nNAME_SPECIFIC"]
  year_2018_T_REGION["year_2018.T_REGION\nTER (PK)\nID_FO\nName"]
  year_2018_T_SECTION["year_2018.T_SECTION\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nCAPTION"]
  year_2018_T_SECTION_Appendix["year_2018.T_SECTION_Appendix\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nCAPTION\n..."]
  year_2018_T_SECTION_ERR["year_2018.T_SECTION_ERR\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nNAME_SHORT\n..."]
  year_2018_T_TITUL_KAT["year_2018.T_TITUL_KAT\nID\nNAME"]
  year_2018_T_TITUL_STATUS["year_2018.T_TITUL_STATUS\nID\nNAME"]
  year_2018_T_TITUL_TYPE["year_2018.T_TITUL_TYPE\nID\nNAME"]
  year_2018_T_TITUL_VID["year_2018.T_TITUL_VID\nID\nNAME"]
  year_2018_T_TYPE_DB["year_2018.T_TYPE_DB\nType_DB"]
  year_2018_T_VERSION["year_2018.T_VERSION\nID\nMajor_Version\nMinor_Version\nRelease_Version\nBulid_Version"]
  year_2018_T_VO["year_2018.T_VO\nVO (PK)\nNAME"]
  year_2018_T_VO_N["year_2018.T_VO_N\nVO\nVO_IBS\nNAME\nSelected"]
  year_2018_T_YEAR["year_2018.T_YEAR\nID"]
  year_2018_test["year_2018.test\nID\nDATA"]
  year_2019_T_Cell_ReadOnly["year_2019.T_Cell_ReadOnly\nID\nID_Form\nID_Section\nID_Col\nID_Row\n..."]
  year_2019_T_Cell_ReadOnly_MON["year_2019.T_Cell_ReadOnly_MON\nID\nID_Form\nID_Section\nID_Col\nID_Row\n..."]
  year_2019_T_DATA["year_2019.T_DATA\nRec (PK)\nID\nID_Form\nID_Vo\nID_Section\n..."]
  year_2019_T_DIC_GROUP_INST["year_2019.T_DIC_GROUP_INST\nID_DIC\nKOD\nNAME\nKOD_NAME\nSelected"]
  year_2019_T_DIC_NAUKA["year_2019.T_DIC_NAUKA\nID_DIC (PK)\nKOD\nNAME\nKod_Kval\nKOD_NAME\n..."]
  year_2019_T_DIC_REPUBLIC["year_2019.T_DIC_REPUBLIC\nID_DIC\nKOD (PK)\nID_Type\nName\nKOD_NAME\n..."]
  year_2019_T_DIC_SPEC["year_2019.T_DIC_SPEC\nID_DIC (PK)\nKOD\nKod_Kval\nNAME\nKOD_NAME\n..."]
  year_2019_T_DIC_SPECIFIC["year_2019.T_DIC_SPECIFIC\nID_DIC\nKOD\nNAME\nNAME_F"]
  year_2019_T_DIC_SPEC_CLOSED["year_2019.T_DIC_SPEC_CLOSED\nID_DIC"]
  year_2019_T_DIC_SPEC_SPECIFIC["year_2019.T_DIC_SPEC_SPECIFIC\nID_DIC\nKOD\nKod_Kval\nNAME\nKOD_NAME\n..."]
  year_2019_T_DIC_UGS["year_2019.T_DIC_UGS\nID_DIC\nKOD\nNAME\nID_OTRASL"]
  year_2019_T_ERROR["year_2019.T_ERROR\nID\nForm_ID\nVO_ID\nSection_ID\nSTRK\n..."]
  year_2019_T_FO["year_2019.T_FO\nNFO (PK)\nNAME"]
  year_2019_T_Form_Cell["year_2019.T_Form_Cell\nID\nID_Col\nID_Row\nDic_Source\nFormat_Cell\n..."]
  year_2019_T_Form_Col["year_2019.T_Form_Col\nID\nID_Form\nID_Section\nID_Column_Num\nID_Type_Col\n..."]
  year_2019_T_Form_Col_Appendix["year_2019.T_Form_Col_Appendix\nID\nID_Form\nID_Section\nID_Column_Num\nID_Type_Col\n..."]
  year_2019_T_Form_Col_SumTotal["year_2019.T_Form_Col_SumTotal\nID\nID_FORM\nID_SECTION\nID_COL_NUM_DEST\nID_COL_NUM_CURRENT\n..."]
  year_2019_T_Form_Register["year_2019.T_Form_Register\nID\nID_Form\nID_Inst\nID_User\nForm_Status\n..."]
  year_2019_T_Form_Row["year_2019.T_Form_Row\nID (PK)\nID_FORM\nID_SECTION\nSECTION_TYPE\nID_ROW_NUM\n..."]
  year_2019_T_Form_Row_SumTotal["year_2019.T_Form_Row_SumTotal\nID\nID_FORM\nID_SECTION\nID_ROW_NUM_TOTAL\nID_ROW_NUM_SUM\n..."]
  year_2019_T_Form_SumTotal["year_2019.T_Form_SumTotal\nID\nID_FORM\nID_SECTION\nID_ROW_TOTAL\nID_COL_NUM_DEST\n..."]
  year_2019_T_Forms["year_2019.T_Forms\nID\nOKUD\nName\nShort_Name\nData_Start\n..."]
  year_2019_T_INSTITUTION["year_2019.T_INSTITUTION\nID (PK)\nParent_ID\npzk\nName\nter\n..."]
  year_2019_T_LIST_FIL["year_2019.T_LIST_FIL\nREC\nID\nName\nTYPE\nOKATO\n..."]
  year_2019_T_LIST_UCH["year_2019.T_LIST_UCH\nREC\nID\nName\nPOST\nKOD_TEL\n..."]
  year_2019_T_OU_SPECIFIC["year_2019.T_OU_SPECIFIC\nID_OU\nNAME_OU\nKOD_SPECIFIC\nNAME_SPECIFIC"]
  year_2019_T_REGION["year_2019.T_REGION\nTER (PK)\nID_FO\nName"]
  year_2019_T_SECTION["year_2019.T_SECTION\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nCAPTION"]
  year_2019_T_SECTION_Appendix["year_2019.T_SECTION_Appendix\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nCAPTION\n..."]
  year_2019_T_SECTION_ERR["year_2019.T_SECTION_ERR\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nNAME_SHORT\n..."]
  year_2019_T_TITUL_KAT["year_2019.T_TITUL_KAT\nID\nNAME"]
  year_2019_T_TITUL_STATUS["year_2019.T_TITUL_STATUS\nID\nNAME"]
  year_2019_T_TITUL_TYPE["year_2019.T_TITUL_TYPE\nID\nNAME"]
  year_2019_T_TITUL_VID["year_2019.T_TITUL_VID\nID\nNAME"]
  year_2019_T_TYPE_DB["year_2019.T_TYPE_DB\nType_DB"]
  year_2019_T_VERSION["year_2019.T_VERSION\nID\nMajor_Version\nMinor_Version\nRelease_Version\nBulid_Version"]
  year_2019_T_VO["year_2019.T_VO\nVO (PK)\nNAME"]
  year_2019_T_VO_N["year_2019.T_VO_N\nVO\nVO_IBS\nNAME\nSelected"]
  year_2019_T_YEAR["year_2019.T_YEAR\nID"]
  year_2020_T_Cell_ReadOnly["year_2020.T_Cell_ReadOnly\nID\nID_Form\nID_Section\nID_Col\nID_Row\n..."]
  year_2020_T_Cell_ReadOnly_MON["year_2020.T_Cell_ReadOnly_MON\nID\nID_Form\nID_Section\nID_Col\nID_Row\n..."]
  year_2020_T_Cell_ReadOnly_MON_za2019["year_2020.T_Cell_ReadOnly_MON_za2019\nID\nID_Form\nID_Section\nID_Col\nID_Row\n..."]
  year_2020_T_DATA["year_2020.T_DATA\nRec (PK)\nID\nID_Form\nID_Vo\nID_Section\n..."]
  year_2020_T_DIC_GROUP_INST["year_2020.T_DIC_GROUP_INST\nID_DIC\nKOD\nNAME\nKOD_NAME\nSelected"]
  year_2020_T_DIC_NAUKA["year_2020.T_DIC_NAUKA\nID_DIC (PK)\nKOD\nNAME\nKod_Kval\nKOD_NAME\n..."]
  year_2020_T_DIC_REPUBLIC["year_2020.T_DIC_REPUBLIC\nID_DIC\nKOD (PK)\nID_Type\nName\nKOD_NAME\n..."]
  year_2020_T_DIC_SPEC["year_2020.T_DIC_SPEC\nID_DIC (PK)\nKOD\nKod_Kval\nNAME\nKOD_NAME\n..."]
  year_2020_T_DIC_SPECIFIC["year_2020.T_DIC_SPECIFIC\nID_DIC\nKOD\nNAME\nNAME_F"]
  year_2020_T_DIC_SPEC_CLOSED["year_2020.T_DIC_SPEC_CLOSED\nID_DIC"]
  year_2020_T_DIC_SPEC_SPECIFIC["year_2020.T_DIC_SPEC_SPECIFIC\nID_DIC\nKOD\nKod_Kval\nNAME\nKOD_NAME\n..."]
  year_2020_T_DIC_UGS["year_2020.T_DIC_UGS\nID_DIC\nKOD\nNAME\nID_OTRASL"]
  year_2020_T_ERROR["year_2020.T_ERROR\nID\nForm_ID\nVO_ID\nSection_ID\nSTRK\n..."]
  year_2020_T_FO["year_2020.T_FO\nNFO (PK)\nNAME"]
  year_2020_T_Form_Cell["year_2020.T_Form_Cell\nID\nID_Col\nID_Row\nDic_Source\nFormat_Cell\n..."]
  year_2020_T_Form_Col["year_2020.T_Form_Col\nID\nID_Form\nID_Section\nID_Column_Num\nID_Type_Col\n..."]
  year_2020_T_Form_Col_Appendix["year_2020.T_Form_Col_Appendix\nID\nID_Form\nID_Section\nID_Column_Num\nID_Type_Col\n..."]
  year_2020_T_Form_Col_SumTotal["year_2020.T_Form_Col_SumTotal\nID\nID_FORM\nID_SECTION\nID_COL_NUM_DEST\nID_COL_NUM_CURRENT\n..."]
  year_2020_T_Form_Register["year_2020.T_Form_Register\nID\nID_Form\nID_Inst\nID_User\nForm_Status\n..."]
  year_2020_T_Form_Row["year_2020.T_Form_Row\nID\nID_FORM\nID_SECTION\nSECTION_TYPE\nID_ROW_NUM\n..."]
  year_2020_T_Form_Row_SumTotal["year_2020.T_Form_Row_SumTotal\nID\nID_FORM\nID_SECTION\nID_ROW_NUM_TOTAL\nID_ROW_NUM_SUM\n..."]
  year_2020_T_Form_SumTotal["year_2020.T_Form_SumTotal\nID\nID_FORM\nID_SECTION\nID_ROW_TOTAL\nID_COL_NUM_DEST\n..."]
  year_2020_T_Forms["year_2020.T_Forms\nID\nOKUD\nName\nShort_Name\nData_Start\n..."]
  year_2020_T_INSTITUTION["year_2020.T_INSTITUTION\nID (PK)\nParent_ID\npzk\nName\nter\n..."]
  year_2020_T_LIST_FIL["year_2020.T_LIST_FIL\nREC\nID\nName\nTYPE\nOKATO\n..."]
  year_2020_T_LIST_UCH["year_2020.T_LIST_UCH\nREC\nID\nName\nPOST\nKOD_TEL\n..."]
  year_2020_T_OU_SPECIFIC["year_2020.T_OU_SPECIFIC\nID_OU\nNAME_OU\nKOD_SPECIFIC\nNAME_SPECIFIC"]
  year_2020_T_REGION["year_2020.T_REGION\nTER (PK)\nID_FO\nName"]
  year_2020_T_SECTION["year_2020.T_SECTION\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nCAPTION"]
  year_2020_T_SECTION_Appendix["year_2020.T_SECTION_Appendix\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nCAPTION\n..."]
  year_2020_T_SECTION_ERR["year_2020.T_SECTION_ERR\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nNAME_SHORT\n..."]
  year_2020_T_TITUL_KAT["year_2020.T_TITUL_KAT\nID\nNAME"]
  year_2020_T_TITUL_STATUS["year_2020.T_TITUL_STATUS\nID\nNAME"]
  year_2020_T_TITUL_TYPE["year_2020.T_TITUL_TYPE\nID\nNAME"]
  year_2020_T_TITUL_VID["year_2020.T_TITUL_VID\nID\nNAME"]
  year_2020_T_TYPE_DB["year_2020.T_TYPE_DB\nType_DB"]
  year_2020_T_VERSION["year_2020.T_VERSION\nID\nMajor_Version\nMinor_Version\nRelease_Version\nBulid_Version"]
  year_2020_T_VO["year_2020.T_VO\nVO (PK)\nNAME"]
  year_2020_T_VO_N["year_2020.T_VO_N\nVO\nVO_IBS\nNAME\nSelected"]
  year_2020_T_YEAR["year_2020.T_YEAR\nID"]
  year_2021_T_Cell_ReadOnly["year_2021.T_Cell_ReadOnly\nID\nID_Form\nID_Section\nID_Col\nID_Row\n..."]
  year_2021_T_Cell_ReadOnly_MON["year_2021.T_Cell_ReadOnly_MON\nID\nID_Form\nID_Section\nID_Col\nID_Row\n..."]
  year_2021_T_DATA["year_2021.T_DATA\nRec (PK)\nID\nID_Form\nID_Vo\nID_Section\n..."]
  year_2021_T_DIC_GROUP_INST["year_2021.T_DIC_GROUP_INST\nID_DIC\nKOD\nNAME\nKOD_NAME\nSelected"]
  year_2021_T_DIC_NAUKA["year_2021.T_DIC_NAUKA\nID_DIC (PK)\nKOD\nNAME\nKod_Kval\nKOD_NAME\n..."]
  year_2021_T_DIC_REPUBLIC["year_2021.T_DIC_REPUBLIC\nID_DIC\nKOD (PK)\nID_Type\nName\nKOD_NAME\n..."]
  year_2021_T_DIC_SPEC["year_2021.T_DIC_SPEC\nID_DIC (PK)\nKOD\nKod_Kval\nNAME\nKOD_NAME\n..."]
  year_2021_T_DIC_SPECIFIC["year_2021.T_DIC_SPECIFIC\nID_DIC\nKOD\nNAME\nNAME_F"]
  year_2021_T_DIC_SPEC_CLOSED["year_2021.T_DIC_SPEC_CLOSED\nID_DIC"]
  year_2021_T_DIC_SPEC_SPECIFIC["year_2021.T_DIC_SPEC_SPECIFIC\nID_DIC\nKOD\nKod_Kval\nNAME\nKOD_NAME\n..."]
  year_2021_T_DIC_UGS["year_2021.T_DIC_UGS\nID_DIC\nKOD\nNAME\nID_OTRASL"]
  year_2021_T_ERROR["year_2021.T_ERROR\nID\nForm_ID\nVO_ID\nSection_ID\nSTRK\n..."]
  year_2021_T_FO["year_2021.T_FO\nNFO (PK)\nNAME\nK"]
  year_2021_T_Form_Cell["year_2021.T_Form_Cell\nID\nID_Col\nID_Row\nDic_Source\nFormat_Cell\n..."]
  year_2021_T_Form_Col["year_2021.T_Form_Col\nID\nID_Form\nID_Section\nID_Column_Num\nID_Type_Col\n..."]
  year_2021_T_Form_Col_Appendix["year_2021.T_Form_Col_Appendix\nID\nID_Form\nID_Section\nID_Column_Num\nID_Type_Col\n..."]
  year_2021_T_Form_Col_SumTotal["year_2021.T_Form_Col_SumTotal\nID\nID_FORM\nID_SECTION\nID_COL_NUM_DEST\nID_COL_NUM_CURRENT\n..."]
  year_2021_T_Form_Register["year_2021.T_Form_Register\nID\nID_Form\nID_Inst\nID_User\nForm_Status\n..."]
  year_2021_T_Form_Row["year_2021.T_Form_Row\nID\nID_FORM\nID_SECTION\nSECTION_TYPE\nID_ROW_NUM\n..."]
  year_2021_T_Form_Row_SumTotal["year_2021.T_Form_Row_SumTotal\nID\nID_FORM\nID_SECTION\nID_ROW_NUM_TOTAL\nID_ROW_NUM_SUM\n..."]
  year_2021_T_Form_SumTotal["year_2021.T_Form_SumTotal\nID\nID_FORM\nID_SECTION\nID_ROW_TOTAL\nID_COL_NUM_DEST\n..."]
  year_2021_T_Forms["year_2021.T_Forms\nID\nOKUD\nName\nShort_Name\nData_Start\n..."]
  year_2021_T_INSTITUTION["year_2021.T_INSTITUTION\nID (PK)\nParent_ID\npzk\nName\nTER\n..."]
  year_2021_T_LIST_UCH["year_2021.T_LIST_UCH\nREC\nID\nName\nPOST\nKOD_TEL\n..."]
  year_2021_T_OU_SPECIFIC["year_2021.T_OU_SPECIFIC\nID_OU\nNAME_OU\nKOD_SPECIFIC\nNAME_SPECIFIC"]
  year_2021_T_REGION["year_2021.T_REGION\nTER (PK)\nID_FO\nER\nName"]
  year_2021_T_SECTION["year_2021.T_SECTION\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nCAPTION"]
  year_2021_T_SECTION_Appendix["year_2021.T_SECTION_Appendix\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nCAPTION\n..."]
  year_2021_T_SECTION_ERR["year_2021.T_SECTION_ERR\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nNAME_SHORT\n..."]
  year_2021_T_TITUL_KAT["year_2021.T_TITUL_KAT\nID\nNAME"]
  year_2021_T_TITUL_STATUS["year_2021.T_TITUL_STATUS\nID\nNAME"]
  year_2021_T_TITUL_TYPE["year_2021.T_TITUL_TYPE\nID\nNAME"]
  year_2021_T_TITUL_VID["year_2021.T_TITUL_VID\nID\nNAME"]
  year_2021_T_TYPE_DB["year_2021.T_TYPE_DB\nType_DB"]
  year_2021_T_VERSION["year_2021.T_VERSION\nID\nMajor_Version\nMinor_Version\nRelease_Version\nBulid_Version"]
  year_2021_T_VO["year_2021.T_VO\nVO (PK)\nNAME"]
  year_2021_T_VO_N["year_2021.T_VO_N\nVO\nVO_IBS\nNAME\nSelected"]
  year_2021_T_YEAR["year_2021.T_YEAR\nID"]
  year_2022_T_Cell_ReadOnly["year_2022.T_Cell_ReadOnly\nID\nID_Form\nID_Section\nID_Col\nID_Row\n..."]
  year_2022_T_Cell_ReadOnly_MON["year_2022.T_Cell_ReadOnly_MON\nID\nID_Form\nID_Section\nID_Col\nID_Row\n..."]
  year_2022_T_DATA["year_2022.T_DATA\nRec (PK)\nID\nID_Form\nID_Vo\nID_Section\n..."]
  year_2022_T_DIC_GROUP_INST["year_2022.T_DIC_GROUP_INST\nID_DIC\nKOD\nNAME\nKOD_NAME\nSelected"]
  year_2022_T_DIC_NAUKA["year_2022.T_DIC_NAUKA\nID_DIC (PK)\nKOD\nNAME\nKod_Kval\nKOD_NAME\n..."]
  year_2022_T_DIC_REPUBLIC["year_2022.T_DIC_REPUBLIC\nID_DIC\nKOD (PK)\nID_Type\nName\nKOD_NAME\n..."]
  year_2022_T_DIC_SPEC["year_2022.T_DIC_SPEC\nID_DIC (PK)\nKOD\nKod_Kval\nNAME\nKOD_NAME\n..."]
  year_2022_T_DIC_SPECIFIC["year_2022.T_DIC_SPECIFIC\nID_DIC (PK)\nKOD\nNAME\nNAME_F"]
  year_2022_T_DIC_SPEC_CLOSED["year_2022.T_DIC_SPEC_CLOSED\nID_DIC (PK)"]
  year_2022_T_DIC_SPEC_SPECIFIC["year_2022.T_DIC_SPEC_SPECIFIC\nID_DIC (PK)\nKOD\nKod_Kval\nNAME\nKOD_NAME\n..."]
  year_2022_T_DIC_UGS["year_2022.T_DIC_UGS\nID_DIC\nKOD\nNAME\nID_OTRASL"]
  year_2022_T_ERROR["year_2022.T_ERROR\nID\nForm_ID\nVO_ID\nSection_ID\nSTRK\n..."]
  year_2022_T_FO["year_2022.T_FO\nNFO (PK)\nNAME"]
  year_2022_T_Form_Cell["year_2022.T_Form_Cell\nID (PK)\nID_Col\nID_Row\nDic_Source\nFormat_Cell\n..."]
  year_2022_T_Form_Col["year_2022.T_Form_Col\nID (PK)\nID_Form\nID_Section\nID_Column_Num\nID_Type_Col\n..."]
  year_2022_T_Form_Col_Appendix["year_2022.T_Form_Col_Appendix\nID (PK)\nID_Form\nID_Section\nID_Column_Num\nID_Type_Col\n..."]
  year_2022_T_Form_Col_SumTotal["year_2022.T_Form_Col_SumTotal\nID (PK)\nID_FORM\nID_SECTION\nID_COL_NUM_DEST\nID_COL_NUM_CURRENT\n..."]
  year_2022_T_Form_Register["year_2022.T_Form_Register\nID (PK)\nID_Form\nID_Inst\nID_User\nForm_Status\n..."]
  year_2022_T_Form_Row["year_2022.T_Form_Row\nID (PK)\nID_FORM\nID_SECTION\nSECTION_TYPE\nID_ROW_NUM\n..."]
  year_2022_T_Form_Row_SumTotal["year_2022.T_Form_Row_SumTotal\nID (PK)\nID_FORM\nID_SECTION\nID_ROW_NUM_TOTAL\nID_ROW_NUM_SUM\n..."]
  year_2022_T_Form_SumTotal["year_2022.T_Form_SumTotal\nID (PK)\nID_FORM\nID_SECTION\nID_ROW_TOTAL\nID_COL_NUM_DEST\n..."]
  year_2022_T_Forms["year_2022.T_Forms\nID (PK)\nOKUD\nName\nShort_Name\nData_Start\n..."]
  year_2022_T_INSTITUTION["year_2022.T_INSTITUTION\nID (PK)\nParent_ID\npzk\nName\nTER\n..."]
  year_2022_T_LIST_FIL["year_2022.T_LIST_FIL\nREC (PK)\nID\nName\nTYPE\nOKATO\n..."]
  year_2022_T_LIST_UCH["year_2022.T_LIST_UCH\nREC (PK)\nID\nName\nPOST\nKOD_TEL\n..."]
  year_2022_T_OU_SPECIFIC["year_2022.T_OU_SPECIFIC\nID_OU\nNAME_OU\nKOD_SPECIFIC\nNAME_SPECIFIC"]
  year_2022_T_REGION["year_2022.T_REGION\nTER (PK)\nID_FO\nER\nName"]
  year_2022_T_SECTION["year_2022.T_SECTION\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nCAPTION"]
  year_2022_T_SECTION_Appendix["year_2022.T_SECTION_Appendix\nID_FORM (PK)\nID_SECTION (PK)\nID_TYPE\nNAME\nCAPTION\n..."]
  year_2022_T_SECTION_ERR["year_2022.T_SECTION_ERR\nID_FORM\nID_SECTION\nID_TYPE\nNAME\nNAME_SHORT\n..."]
  year_2022_T_TITUL_KAT["year_2022.T_TITUL_KAT\nID (PK)\nNAME"]
  year_2022_T_TITUL_STATUS["year_2022.T_TITUL_STATUS\nID (PK)\nNAME"]
  year_2022_T_TITUL_TYPE["year_2022.T_TITUL_TYPE\nID (PK)\nNAME"]
  year_2022_T_TITUL_VID["year_2022.T_TITUL_VID\nID (PK)\nNAME"]
  year_2022_T_TYPE_DB["year_2022.T_TYPE_DB\nType_DB"]
  year_2022_T_VERSION["year_2022.T_VERSION\nID (PK)\nMajor_Version\nMinor_Version\nRelease_Version\nBulid_Version"]
  year_2022_T_VO["year_2022.T_VO\nVO (PK)\nNAME"]
  year_2022_T_VO_N["year_2022.T_VO_N\nVO (PK)\nVO_IBS\nNAME\nSelected"]
  year_2022_T_YEAR["year_2022.T_YEAR\nID"]
  year_2022_dbo_T_Institute_vpo["year_2022.dbo_T_Institute_vpo\nID\nID_Parent\nID_CITIS\nNAME\ninst_destroy\n..."]
  year_2023_T_DATA["year_2023.T_DATA\nID\nID_Vo\nID_Section\nID_Row\nDic_Val\n..."]
  year_2023_T_DIC_NAUKA["year_2023.T_DIC_NAUKA\nID_DIC (PK)\nKOD\nNAME\nKOD_NAME\nTYPE\n..."]
  year_2023_T_DIC_REPUBLIC["year_2023.T_DIC_REPUBLIC\nID_DIC\nKOD (PK)\nName\nKOD_NAME"]
  year_2023_T_DIC_SPEC["year_2023.T_DIC_SPEC\nID_DIC (PK)\nKOD\nKod_Kval\nNAME\nKOD_NAME\n..."]
  year_2023_T_DIC_UGS["year_2023.T_DIC_UGS\nID_DIC\nKOD\nNAME"]
  year_2023_T_FO["year_2023.T_FO\nNFO (PK)\nNAME"]
  year_2023_T_INSTITUTION["year_2023.T_INSTITUTION\nID (PK)\nParent_ID\npzk\nName\nTER\n..."]
  year_2023_T_REGION["year_2023.T_REGION\nTER (PK)\nName"]
  year_2023_T_SECTION["year_2023.T_SECTION\nID_SECTION\nNAME\nNAME_SHORT\nCAPTION"]
  year_2023_T_VO["year_2023.T_VO\nVO (PK)\nNAME"]
```

## Problems

- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_Cell_ReadOnly`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_Cell_ReadOnly_MON`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_DIC_GROUP_INST`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_DIC_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_DIC_SPEC_CLOSED`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_DIC_SPEC_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_DIC_UGS`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_ERROR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_Form_Cell`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_Form_Col`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_Form_Col_Appendix`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_Form_Col_SumTotal`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_Form_Register`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_Form_Row_SumTotal`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_Form_SumTotal`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_Forms`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_LIST_FIL`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_LIST_UCH`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_OU_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_SECTION`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_SECTION_Appendix`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_SECTION_ERR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_TITUL_KAT`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_TITUL_STATUS`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_TITUL_TYPE`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_TITUL_VID`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_TYPE_DB`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_VERSION`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_VO_N`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.T_YEAR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2018.test`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_Cell_ReadOnly`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_Cell_ReadOnly_MON`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_DIC_GROUP_INST`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_DIC_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_DIC_SPEC_CLOSED`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_DIC_SPEC_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_DIC_UGS`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_ERROR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_Form_Cell`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_Form_Col`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_Form_Col_Appendix`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_Form_Col_SumTotal`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_Form_Register`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_Form_Row_SumTotal`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_Form_SumTotal`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_Forms`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_LIST_FIL`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_LIST_UCH`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_OU_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_SECTION`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_SECTION_Appendix`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_SECTION_ERR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_TITUL_KAT`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_TITUL_STATUS`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_TITUL_TYPE`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_TITUL_VID`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_TYPE_DB`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_VERSION`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_VO_N`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2019.T_YEAR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_Cell_ReadOnly`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_Cell_ReadOnly_MON`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_Cell_ReadOnly_MON_za2019`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_DIC_GROUP_INST`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_DIC_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_DIC_SPEC_CLOSED`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_DIC_SPEC_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_DIC_UGS`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_ERROR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_Form_Cell`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_Form_Col`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_Form_Col_Appendix`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_Form_Col_SumTotal`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_Form_Register`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_Form_Row`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_Form_Row_SumTotal`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_Form_SumTotal`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_Forms`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_LIST_FIL`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_LIST_UCH`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_OU_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_SECTION`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_SECTION_Appendix`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_SECTION_ERR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_TITUL_KAT`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_TITUL_STATUS`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_TITUL_TYPE`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_TITUL_VID`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_TYPE_DB`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_VERSION`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_VO_N`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2020.T_YEAR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_Cell_ReadOnly`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_Cell_ReadOnly_MON`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_DIC_GROUP_INST`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_DIC_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_DIC_SPEC_CLOSED`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_DIC_SPEC_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_DIC_UGS`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_ERROR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_Form_Cell`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_Form_Col`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_Form_Col_Appendix`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_Form_Col_SumTotal`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_Form_Register`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_Form_Row`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_Form_Row_SumTotal`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_Form_SumTotal`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_Forms`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_LIST_UCH`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_OU_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_SECTION`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_SECTION_Appendix`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_SECTION_ERR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_TITUL_KAT`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_TITUL_STATUS`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_TITUL_TYPE`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_TITUL_VID`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_TYPE_DB`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_VERSION`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_VO_N`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2021.T_YEAR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2022.T_Cell_ReadOnly`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2022.T_Cell_ReadOnly_MON`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2022.T_DIC_GROUP_INST`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2022.T_DIC_UGS`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2022.T_ERROR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2022.T_OU_SPECIFIC`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2022.T_SECTION`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2022.T_SECTION_ERR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2022.T_TYPE_DB`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2022.T_YEAR`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2022.dbo_T_Institute_vpo`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2023.T_DIC_UGS`: Table does not define a primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `year_2023.T_SECTION`: Table does not define a primary key.
- `WARNING` `NO_INDEXES` in `year_2018.T_Cell_ReadOnly`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_Cell_ReadOnly_MON`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_DIC_GROUP_INST`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_DIC_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_DIC_SPEC_CLOSED`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_DIC_SPEC_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_DIC_UGS`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_ERROR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_Form_Cell`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_Form_Col`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_Form_Col_Appendix`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_Form_Col_SumTotal`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_Form_Register`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_Form_Row_SumTotal`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_Form_SumTotal`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_Forms`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_LIST_FIL`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_LIST_UCH`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_OU_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_SECTION`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_SECTION_Appendix`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_SECTION_ERR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_TITUL_KAT`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_TITUL_STATUS`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_TITUL_TYPE`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_TITUL_VID`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_TYPE_DB`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_VERSION`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_VO_N`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.T_YEAR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2018.test`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_Cell_ReadOnly`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_Cell_ReadOnly_MON`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_DIC_GROUP_INST`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_DIC_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_DIC_SPEC_CLOSED`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_DIC_SPEC_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_DIC_UGS`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_ERROR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_Form_Cell`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_Form_Col`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_Form_Col_Appendix`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_Form_Col_SumTotal`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_Form_Register`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_Form_Row_SumTotal`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_Form_SumTotal`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_Forms`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_LIST_FIL`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_LIST_UCH`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_OU_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_SECTION`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_SECTION_Appendix`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_SECTION_ERR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_TITUL_KAT`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_TITUL_STATUS`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_TITUL_TYPE`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_TITUL_VID`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_TYPE_DB`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_VERSION`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_VO_N`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2019.T_YEAR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_Cell_ReadOnly`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_Cell_ReadOnly_MON`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_Cell_ReadOnly_MON_za2019`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_DIC_GROUP_INST`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_DIC_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_DIC_SPEC_CLOSED`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_DIC_SPEC_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_DIC_UGS`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_ERROR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_Form_Cell`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_Form_Col`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_Form_Col_Appendix`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_Form_Col_SumTotal`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_Form_Register`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_Form_Row`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_Form_Row_SumTotal`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_Form_SumTotal`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_Forms`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_LIST_FIL`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_LIST_UCH`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_OU_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_SECTION`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_SECTION_Appendix`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_SECTION_ERR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_TITUL_KAT`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_TITUL_STATUS`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_TITUL_TYPE`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_TITUL_VID`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_TYPE_DB`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_VERSION`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_VO_N`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2020.T_YEAR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_Cell_ReadOnly`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_Cell_ReadOnly_MON`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_DIC_GROUP_INST`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_DIC_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_DIC_SPEC_CLOSED`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_DIC_SPEC_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_DIC_UGS`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_ERROR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_Form_Cell`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_Form_Col`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_Form_Col_Appendix`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_Form_Col_SumTotal`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_Form_Register`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_Form_Row`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_Form_Row_SumTotal`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_Form_SumTotal`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_Forms`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_LIST_UCH`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_OU_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_SECTION`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_SECTION_Appendix`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_SECTION_ERR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_TITUL_KAT`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_TITUL_STATUS`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_TITUL_TYPE`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_TITUL_VID`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_TYPE_DB`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_VERSION`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_VO_N`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2021.T_YEAR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2022.T_Cell_ReadOnly`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2022.T_Cell_ReadOnly_MON`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2022.T_DIC_GROUP_INST`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2022.T_DIC_UGS`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2022.T_ERROR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2022.T_OU_SPECIFIC`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2022.T_SECTION`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2022.T_SECTION_ERR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2022.T_TYPE_DB`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2022.T_YEAR`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2022.dbo_T_Institute_vpo`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2023.T_DIC_UGS`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `NO_INDEXES` in `year_2023.T_SECTION`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_Cell_ReadOnly

- Estimated rows: `349`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `ID_Type_Cell` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_Cell_ReadOnly_MON

- Estimated rows: `943`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `ID_Type_Cell` | `INTEGER` | yes |  |  |
| `Status_Cell` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_DATA

- Estimated rows: `879383`
- Primary key: `Rec`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `Rec` | `INTEGER` | no | `nextval('year_2018."T_DATA_Rec_seq"'::regclass)` | PK, Indexed |
| `ID` | `INTEGER` | yes |  | Indexed |
| `ID_Form` | `INTEGER` | yes |  | Indexed |
| `ID_Vo` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  | Indexed |
| `ID_Row` | `INTEGER` | yes |  | Indexed |
| `Dic_Val` | `INTEGER` | yes |  |  |
| `GR3` | `DOUBLE PRECISION` | yes |  |  |
| `GR4` | `DOUBLE PRECISION` | yes |  |  |
| `GR5` | `DOUBLE PRECISION` | yes |  |  |
| `GR6` | `DOUBLE PRECISION` | yes |  |  |
| `GR7` | `DOUBLE PRECISION` | yes |  |  |
| `GR8` | `DOUBLE PRECISION` | yes |  |  |
| `GR9` | `DOUBLE PRECISION` | yes |  |  |
| `GR10` | `DOUBLE PRECISION` | yes |  |  |
| `GR11` | `DOUBLE PRECISION` | yes |  |  |
| `GR12` | `DOUBLE PRECISION` | yes |  |  |
| `GR13` | `DOUBLE PRECISION` | yes |  |  |
| `GR14` | `DOUBLE PRECISION` | yes |  |  |
| `GR15` | `DOUBLE PRECISION` | yes |  |  |
| `GR16` | `DOUBLE PRECISION` | yes |  |  |
| `GR17` | `DOUBLE PRECISION` | yes |  |  |
| `GR18` | `DOUBLE PRECISION` | yes |  |  |
| `GR19` | `DOUBLE PRECISION` | yes |  |  |
| `GR20` | `DOUBLE PRECISION` | yes |  |  |
| `GR21` | `DOUBLE PRECISION` | yes |  |  |
| `GR22` | `DOUBLE PRECISION` | yes |  |  |
| `GR23` | `DOUBLE PRECISION` | yes |  |  |
| `GR24` | `DOUBLE PRECISION` | yes |  |  |
| `GR25` | `DOUBLE PRECISION` | yes |  |  |
| `GR26` | `DOUBLE PRECISION` | yes |  |  |
| `GR27` | `DOUBLE PRECISION` | yes |  |  |
| `GR28` | `DOUBLE PRECISION` | yes |  |  |
| `GR29` | `DOUBLE PRECISION` | yes |  |  |
| `GR30` | `DOUBLE PRECISION` | yes |  |  |
| `GR31` | `DOUBLE PRECISION` | yes |  |  |
| `GR32` | `DOUBLE PRECISION` | yes |  |  |
| `GR33` | `DOUBLE PRECISION` | yes |  |  |
| `GR34` | `DOUBLE PRECISION` | yes |  |  |
| `GR35` | `DOUBLE PRECISION` | yes |  |  |
| `GR36` | `DOUBLE PRECISION` | yes |  |  |
| `GR37` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DATA_pk_idx` on `ID`, `ID_Form`, `ID_Section`, `ID_Row`
- `T_DATA_pkey` (primary, unique) on `Rec`

### Problems

- None

## year_2018.T_DIC_GROUP_INST

- Estimated rows: `15`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(255)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(50)` | yes |  |  |
| `Selected` | `BIT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_DIC_NAUKA

- Estimated rows: `705`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(20)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(4)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `TYPE` | `VARCHAR(510)` | yes |  |  |
| `Kod_Classifier` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_NAUKA_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2018.T_DIC_REPUBLIC

- Estimated rows: `237`
- Primary key: `KOD`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(12)` | no |  | PK, Indexed |
| `ID_Type` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `Sorting` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_REPUBLIC_pkey` (primary, unique) on `KOD`

### Problems

- None

## year_2018.T_DIC_SPEC

- Estimated rows: `1068`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(16)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(4)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `TYPE` | `VARCHAR(100)` | yes |  |  |
| `Kod_Classifier` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_SPEC_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2018.T_DIC_SPECIFIC

- Estimated rows: `7`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(50)` | yes |  |  |
| `NAME` | `VARCHAR(255)` | yes |  |  |
| `NAME_F` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_DIC_SPEC_CLOSED

- Estimated rows: `60`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_DIC_SPEC_SPECIFIC

- Estimated rows: `328`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(8)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(2)` | yes |  |  |
| `NAME` | `VARCHAR(255)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(255)` | yes |  |  |
| `TYPE` | `VARCHAR(50)` | yes |  |  |
| `Selected` | `BIT` | yes |  |  |
| `Specific` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_DIC_UGS

- Estimated rows: `87`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(510)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `ID_OTRASL` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_ERROR

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `Form_ID` | `INTEGER` | yes |  |  |
| `VO_ID` | `INTEGER` | yes |  |  |
| `Section_ID` | `INTEGER` | yes |  |  |
| `STRK` | `INTEGER` | yes |  |  |
| `DIC_VAL` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `ERR` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_FO

- Estimated rows: `8`
- Primary key: `NFO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `NFO` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_FO_pkey` (primary, unique) on `NFO`

### Problems

- None

## year_2018.T_Form_Cell

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `Dic_Source` | `VARCHAR(50)` | yes |  |  |
| `Format_Cell` | `VARCHAR(50)` | yes |  |  |
| `Default_Val` | `VARCHAR(50)` | yes |  |  |
| `Input_Type` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_Form_Col

- Estimated rows: `555`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Column_Num` | `INTEGER` | yes |  |  |
| `ID_Type_Col` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Width` | `INTEGER` | yes |  |  |
| `Field` | `VARCHAR(50)` | yes |  |  |
| `Alignment` | `VARCHAR(50)` | yes |  |  |
| `FieldType` | `VARCHAR(50)` | yes |  |  |
| `FieldDisplayFormat` | `VARCHAR(50)` | yes |  |  |
| `FieldEditFormat` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_Form_Col_Appendix

- Estimated rows: `59`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Column_Num` | `INTEGER` | yes |  |  |
| `ID_Type_Col` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Width` | `INTEGER` | yes |  |  |
| `Field` | `VARCHAR(50)` | yes |  |  |
| `Alignment` | `VARCHAR(50)` | yes |  |  |
| `FieldType` | `VARCHAR(50)` | yes |  |  |
| `FieldDisplayFormat` | `VARCHAR(50)` | yes |  |  |
| `FieldEditFormat` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_Form_Col_SumTotal

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_COL_NUM_DEST` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_CURRENT` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_PREV` | `VARCHAR(100)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_Form_Register

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Inst` | `INTEGER` | yes |  |  |
| `ID_User` | `INTEGER` | yes |  |  |
| `Form_Status` | `INTEGER` | yes |  |  |
| `DataStart` | `VARCHAR(50)` | yes |  |  |
| `DataEdit` | `VARCHAR(128)` | yes |  |  |
| `Version` | `VARCHAR(50)` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Check` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_Form_Row

- Estimated rows: `520`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no | `nextval('year_2018."T_Form_Row_ID_seq"'::regclass)` | PK, Indexed |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `SECTION_TYPE` | `INTEGER` | yes |  |  |
| `ID_ROW_NUM` | `INTEGER` | yes |  | Indexed |
| `ID_ROW_NUM_Display` | `VARCHAR(100)` | yes |  |  |
| `ID_TYPE_ROW` | `INTEGER` | yes |  |  |
| `NAME_TAB_ROW` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_Form_Row_T_FORM_ROWID_Row_idx` on `ID_ROW_NUM`
- `T_Form_Row_T_FORM_ROWID_idx` on `ID`
- `T_Form_Row_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2018.T_Form_Row_SumTotal

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_ROW_NUM_TOTAL` | `VARCHAR(50)` | yes |  |  |
| `ID_ROW_NUM_SUM` | `VARCHAR(100)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |
| `COL_NUM_TOTAL` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_Form_SumTotal

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_ROW_TOTAL` | `INTEGER` | yes |  |  |
| `ID_COL_NUM_DEST` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_CURRENT` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_PREV` | `VARCHAR(100)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_Forms

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `OKUD` | `VARCHAR(50)` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Short_Name` | `VARCHAR(255)` | yes |  |  |
| `Data_Start` | `VARCHAR(50)` | yes |  |  |
| `Version` | `VARCHAR(50)` | yes |  |  |
| `Order` | `VARCHAR(50)` | yes |  |  |
| `Order_orig` | `TEXT` | yes |  |  |
| `Status` | `BIT` | yes |  |  |
| `Year` | `INTEGER` | yes |  |  |
| `Selfname` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_INSTITUTION

- Estimated rows: `1240`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `Parent_ID` | `INTEGER` | yes |  |  |
| `pzk` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `ter` | `VARCHAR(10)` | yes |  |  |
| `Reg_Name` | `VARCHAR(100)` | yes |  |  |
| `ID_FO` | `INTEGER` | yes |  |  |
| `FO_Name` | `VARCHAR(100)` | yes |  |  |
| `ID_OKOGU` | `INTEGER` | yes |  |  |
| `OKOGU` | `VARCHAR(510)` | yes |  |  |
| `POST` | `VARCHAR(510)` | yes |  |  |
| `Website` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_INSTITUTION_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2018.T_LIST_FIL

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `REC` | `INTEGER` | yes |  |  |
| `ID` | `INTEGER` | yes |  |  |
| `Name` | `TEXT` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |
| `OKATO` | `VARCHAR(50)` | yes |  |  |
| `OKSM` | `VARCHAR(50)` | yes |  |  |
| `KOD_EDU_PROG_1` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_2` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_3` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_4` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_5` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_6` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_7` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_8` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_9` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_10` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_11` | `BIT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_LIST_UCH

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `REC` | `INTEGER` | yes |  |  |
| `ID` | `INTEGER` | yes |  |  |
| `Name` | `TEXT` | yes |  |  |
| `POST` | `VARCHAR(255)` | yes |  |  |
| `KOD_TEL` | `VARCHAR(50)` | yes |  |  |
| `TEL` | `VARCHAR(50)` | yes |  |  |
| `EMAIL` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_OU_SPECIFIC

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_OU` | `INTEGER` | yes |  |  |
| `NAME_OU` | `VARCHAR(255)` | yes |  |  |
| `KOD_SPECIFIC` | `INTEGER` | yes |  |  |
| `NAME_SPECIFIC` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_REGION

- Estimated rows: `103`
- Primary key: `TER`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `TER` | `VARCHAR(10)` | no |  | PK, Indexed |
| `ID_FO` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_REGION_pkey` (primary, unique) on `TER`

### Problems

- None

## year_2018.T_SECTION

- Estimated rows: `51`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(400)` | yes |  |  |
| `CAPTION` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_SECTION_Appendix

- Estimated rows: `13`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(200)` | yes |  |  |
| `CAPTION` | `VARCHAR(255)` | yes |  |  |
| `OKEI` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_SECTION_ERR

- Estimated rows: `52`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(200)` | yes |  |  |
| `NAME_SHORT` | `VARCHAR(50)` | yes |  |  |
| `CAPTION` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_TITUL_KAT

- Estimated rows: `3`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_TITUL_STATUS

- Estimated rows: `3`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_TITUL_TYPE

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_TITUL_VID

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_TYPE_DB

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `Type_DB` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_VERSION

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `Major_Version` | `INTEGER` | yes |  |  |
| `Minor_Version` | `INTEGER` | yes |  |  |
| `Release_Version` | `INTEGER` | yes |  |  |
| `Bulid_Version` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_VO

- Estimated rows: `5`
- Primary key: `VO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `VO` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(200)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_VO_pkey` (primary, unique) on `VO`

### Problems

- None

## year_2018.T_VO_N

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `VO` | `INTEGER` | yes |  |  |
| `VO_IBS` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(100)` | yes |  |  |
| `Selected` | `BIT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.T_YEAR

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2018.test

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  |  |
| `DATA` | `INTEGER` | no |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_Cell_ReadOnly

- Estimated rows: `353`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `ID_Type_Cell` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_Cell_ReadOnly_MON

- Estimated rows: `1309`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `ID_Type_Cell` | `INTEGER` | yes |  |  |
| `Status_Cell` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_DATA

- Estimated rows: `850102`
- Primary key: `Rec`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `Rec` | `INTEGER` | no | `nextval('year_2019."T_DATA_Rec_seq"'::regclass)` | PK, Indexed |
| `ID` | `INTEGER` | yes |  | Indexed |
| `ID_Form` | `INTEGER` | yes |  | Indexed |
| `ID_Vo` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  | Indexed |
| `ID_Row` | `INTEGER` | yes |  | Indexed |
| `Dic_Val` | `INTEGER` | yes |  |  |
| `GR3` | `DOUBLE PRECISION` | yes |  |  |
| `GR4` | `DOUBLE PRECISION` | yes |  |  |
| `GR5` | `DOUBLE PRECISION` | yes |  |  |
| `GR6` | `DOUBLE PRECISION` | yes |  |  |
| `GR7` | `DOUBLE PRECISION` | yes |  |  |
| `GR8` | `DOUBLE PRECISION` | yes |  |  |
| `GR9` | `DOUBLE PRECISION` | yes |  |  |
| `GR10` | `DOUBLE PRECISION` | yes |  |  |
| `GR11` | `DOUBLE PRECISION` | yes |  |  |
| `GR12` | `DOUBLE PRECISION` | yes |  |  |
| `GR13` | `DOUBLE PRECISION` | yes |  |  |
| `GR14` | `DOUBLE PRECISION` | yes |  |  |
| `GR15` | `DOUBLE PRECISION` | yes |  |  |
| `GR16` | `DOUBLE PRECISION` | yes |  |  |
| `GR17` | `DOUBLE PRECISION` | yes |  |  |
| `GR18` | `DOUBLE PRECISION` | yes |  |  |
| `GR19` | `DOUBLE PRECISION` | yes |  |  |
| `GR20` | `DOUBLE PRECISION` | yes |  |  |
| `GR21` | `DOUBLE PRECISION` | yes |  |  |
| `GR22` | `DOUBLE PRECISION` | yes |  |  |
| `GR23` | `DOUBLE PRECISION` | yes |  |  |
| `GR24` | `DOUBLE PRECISION` | yes |  |  |
| `GR25` | `DOUBLE PRECISION` | yes |  |  |
| `GR26` | `DOUBLE PRECISION` | yes |  |  |
| `GR27` | `DOUBLE PRECISION` | yes |  |  |
| `GR28` | `DOUBLE PRECISION` | yes |  |  |
| `GR29` | `DOUBLE PRECISION` | yes |  |  |
| `GR30` | `DOUBLE PRECISION` | yes |  |  |
| `GR31` | `DOUBLE PRECISION` | yes |  |  |
| `GR32` | `DOUBLE PRECISION` | yes |  |  |
| `GR33` | `DOUBLE PRECISION` | yes |  |  |
| `GR34` | `DOUBLE PRECISION` | yes |  |  |
| `GR35` | `DOUBLE PRECISION` | yes |  |  |
| `GR36` | `DOUBLE PRECISION` | yes |  |  |
| `GR37` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DATA_pk_idx` on `ID`, `ID_Form`, `ID_Section`, `ID_Row`
- `T_DATA_pkey` (primary, unique) on `Rec`

### Problems

- None

## year_2019.T_DIC_GROUP_INST

- Estimated rows: `15`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(255)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(50)` | yes |  |  |
| `Selected` | `BIT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_DIC_NAUKA

- Estimated rows: `643`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(20)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(4)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `TYPE` | `VARCHAR(510)` | yes |  |  |
| `Kod_Classifier` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_NAUKA_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2019.T_DIC_REPUBLIC

- Estimated rows: `241`
- Primary key: `KOD`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(12)` | no |  | PK, Indexed |
| `ID_Type` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `Sorting` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_REPUBLIC_pkey` (primary, unique) on `KOD`

### Problems

- None

## year_2019.T_DIC_SPEC

- Estimated rows: `1083`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(16)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(4)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `TYPE` | `VARCHAR(100)` | yes |  |  |
| `Kod_Classifier` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_SPEC_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2019.T_DIC_SPECIFIC

- Estimated rows: `7`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(50)` | yes |  |  |
| `NAME` | `VARCHAR(255)` | yes |  |  |
| `NAME_F` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_DIC_SPEC_CLOSED

- Estimated rows: `60`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_DIC_SPEC_SPECIFIC

- Estimated rows: `328`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(8)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(2)` | yes |  |  |
| `NAME` | `VARCHAR(255)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(255)` | yes |  |  |
| `TYPE` | `VARCHAR(50)` | yes |  |  |
| `Selected` | `BIT` | yes |  |  |
| `Specific` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_DIC_UGS

- Estimated rows: `86`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(510)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `ID_OTRASL` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_ERROR

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `Form_ID` | `INTEGER` | yes |  |  |
| `VO_ID` | `INTEGER` | yes |  |  |
| `Section_ID` | `INTEGER` | yes |  |  |
| `STRK` | `INTEGER` | yes |  |  |
| `DIC_VAL` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `ERR` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_FO

- Estimated rows: `8`
- Primary key: `NFO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `NFO` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_FO_pkey` (primary, unique) on `NFO`

### Problems

- None

## year_2019.T_Form_Cell

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `Dic_Source` | `VARCHAR(50)` | yes |  |  |
| `Format_Cell` | `VARCHAR(50)` | yes |  |  |
| `Default_Val` | `VARCHAR(50)` | yes |  |  |
| `Input_Type` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_Form_Col

- Estimated rows: `556`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Column_Num` | `INTEGER` | yes |  |  |
| `ID_Type_Col` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Width` | `INTEGER` | yes |  |  |
| `Field` | `VARCHAR(50)` | yes |  |  |
| `Alignment` | `VARCHAR(50)` | yes |  |  |
| `FieldType` | `VARCHAR(50)` | yes |  |  |
| `FieldDisplayFormat` | `VARCHAR(50)` | yes |  |  |
| `FieldEditFormat` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_Form_Col_Appendix

- Estimated rows: `59`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Column_Num` | `INTEGER` | yes |  |  |
| `ID_Type_Col` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Width` | `INTEGER` | yes |  |  |
| `Field` | `VARCHAR(50)` | yes |  |  |
| `Alignment` | `VARCHAR(50)` | yes |  |  |
| `FieldType` | `VARCHAR(50)` | yes |  |  |
| `FieldDisplayFormat` | `VARCHAR(50)` | yes |  |  |
| `FieldEditFormat` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_Form_Col_SumTotal

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_COL_NUM_DEST` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_CURRENT` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_PREV` | `VARCHAR(100)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_Form_Register

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Inst` | `INTEGER` | yes |  |  |
| `ID_User` | `INTEGER` | yes |  |  |
| `Form_Status` | `INTEGER` | yes |  |  |
| `DataStart` | `VARCHAR(50)` | yes |  |  |
| `DataEdit` | `VARCHAR(128)` | yes |  |  |
| `Version` | `VARCHAR(50)` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Check` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_Form_Row

- Estimated rows: `521`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no | `nextval('year_2019."T_Form_Row_ID_seq"'::regclass)` | PK, Indexed |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `SECTION_TYPE` | `INTEGER` | yes |  |  |
| `ID_ROW_NUM` | `INTEGER` | yes |  | Indexed |
| `ID_ROW_NUM_Display` | `VARCHAR(100)` | yes |  |  |
| `ID_TYPE_ROW` | `INTEGER` | yes |  |  |
| `NAME_TAB_ROW` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_Form_Row_T_FORM_ROWID_Row_idx` on `ID_ROW_NUM`
- `T_Form_Row_T_FORM_ROWID_idx` on `ID`
- `T_Form_Row_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2019.T_Form_Row_SumTotal

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_ROW_NUM_TOTAL` | `VARCHAR(50)` | yes |  |  |
| `ID_ROW_NUM_SUM` | `VARCHAR(100)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |
| `COL_NUM_TOTAL` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_Form_SumTotal

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_ROW_TOTAL` | `INTEGER` | yes |  |  |
| `ID_COL_NUM_DEST` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_CURRENT` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_PREV` | `VARCHAR(100)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_Forms

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `OKUD` | `VARCHAR(50)` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Short_Name` | `VARCHAR(255)` | yes |  |  |
| `Data_Start` | `VARCHAR(50)` | yes |  |  |
| `Version` | `VARCHAR(50)` | yes |  |  |
| `Order` | `VARCHAR(50)` | yes |  |  |
| `Order_orig` | `TEXT` | yes |  |  |
| `Status` | `BIT` | yes |  |  |
| `Year` | `INTEGER` | yes |  |  |
| `Selfname` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_INSTITUTION

- Estimated rows: `1218`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `Parent_ID` | `INTEGER` | yes |  |  |
| `pzk` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `ter` | `VARCHAR(10)` | yes |  |  |
| `Reg_Name` | `VARCHAR(100)` | yes |  |  |
| `ID_FO` | `INTEGER` | yes |  |  |
| `FO_Name` | `VARCHAR(100)` | yes |  |  |
| `ID_OKOGU` | `INTEGER` | yes |  |  |
| `OKOGU` | `VARCHAR(510)` | yes |  |  |
| `POST` | `VARCHAR(510)` | yes |  |  |
| `Website` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_INSTITUTION_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2019.T_LIST_FIL

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `REC` | `INTEGER` | yes |  |  |
| `ID` | `INTEGER` | yes |  |  |
| `Name` | `TEXT` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |
| `OKATO` | `VARCHAR(50)` | yes |  |  |
| `OKSM` | `VARCHAR(50)` | yes |  |  |
| `KOD_EDU_PROG_1` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_2` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_3` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_4` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_5` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_6` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_7` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_8` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_9` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_10` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_11` | `BIT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_LIST_UCH

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `REC` | `INTEGER` | yes |  |  |
| `ID` | `INTEGER` | yes |  |  |
| `Name` | `TEXT` | yes |  |  |
| `POST` | `VARCHAR(255)` | yes |  |  |
| `KOD_TEL` | `VARCHAR(50)` | yes |  |  |
| `TEL` | `VARCHAR(50)` | yes |  |  |
| `EMAIL` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_OU_SPECIFIC

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_OU` | `INTEGER` | yes |  |  |
| `NAME_OU` | `VARCHAR(255)` | yes |  |  |
| `KOD_SPECIFIC` | `INTEGER` | yes |  |  |
| `NAME_SPECIFIC` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_REGION

- Estimated rows: `86`
- Primary key: `TER`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `TER` | `VARCHAR(10)` | no |  | PK, Indexed |
| `ID_FO` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_REGION_pkey` (primary, unique) on `TER`

### Problems

- None

## year_2019.T_SECTION

- Estimated rows: `51`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(400)` | yes |  |  |
| `CAPTION` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_SECTION_Appendix

- Estimated rows: `13`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(200)` | yes |  |  |
| `CAPTION` | `VARCHAR(255)` | yes |  |  |
| `OKEI` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_SECTION_ERR

- Estimated rows: `52`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(200)` | yes |  |  |
| `NAME_SHORT` | `VARCHAR(50)` | yes |  |  |
| `CAPTION` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_TITUL_KAT

- Estimated rows: `3`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_TITUL_STATUS

- Estimated rows: `3`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_TITUL_TYPE

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_TITUL_VID

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_TYPE_DB

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `Type_DB` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_VERSION

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `Major_Version` | `INTEGER` | yes |  |  |
| `Minor_Version` | `INTEGER` | yes |  |  |
| `Release_Version` | `INTEGER` | yes |  |  |
| `Bulid_Version` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_VO

- Estimated rows: `5`
- Primary key: `VO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `VO` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(200)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_VO_pkey` (primary, unique) on `VO`

### Problems

- None

## year_2019.T_VO_N

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `VO` | `INTEGER` | yes |  |  |
| `VO_IBS` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(100)` | yes |  |  |
| `Selected` | `BIT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2019.T_YEAR

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_Cell_ReadOnly

- Estimated rows: `353`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `ID_Type_Cell` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_Cell_ReadOnly_MON

- Estimated rows: `947`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `ID_Type_Cell` | `INTEGER` | yes |  |  |
| `Status_Cell` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_Cell_ReadOnly_MON_za2019

- Estimated rows: `1309`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `ID_Type_Cell` | `INTEGER` | yes |  |  |
| `Status_Cell` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_DATA

- Estimated rows: `858704`
- Primary key: `Rec`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `Rec` | `INTEGER` | no | `nextval('year_2020."T_DATA_Rec_seq"'::regclass)` | PK, Indexed |
| `ID` | `INTEGER` | yes |  | Indexed |
| `ID_Form` | `INTEGER` | yes |  | Indexed |
| `ID_Vo` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  | Indexed |
| `ID_Row` | `INTEGER` | yes |  | Indexed |
| `Dic_Val` | `INTEGER` | yes |  |  |
| `GR3` | `DOUBLE PRECISION` | yes |  |  |
| `GR4` | `DOUBLE PRECISION` | yes |  |  |
| `GR5` | `DOUBLE PRECISION` | yes |  |  |
| `GR6` | `DOUBLE PRECISION` | yes |  |  |
| `GR7` | `DOUBLE PRECISION` | yes |  |  |
| `GR8` | `DOUBLE PRECISION` | yes |  |  |
| `GR9` | `DOUBLE PRECISION` | yes |  |  |
| `GR10` | `DOUBLE PRECISION` | yes |  |  |
| `GR11` | `DOUBLE PRECISION` | yes |  |  |
| `GR12` | `DOUBLE PRECISION` | yes |  |  |
| `GR13` | `DOUBLE PRECISION` | yes |  |  |
| `GR14` | `DOUBLE PRECISION` | yes |  |  |
| `GR15` | `DOUBLE PRECISION` | yes |  |  |
| `GR16` | `DOUBLE PRECISION` | yes |  |  |
| `GR17` | `DOUBLE PRECISION` | yes |  |  |
| `GR18` | `DOUBLE PRECISION` | yes |  |  |
| `GR19` | `DOUBLE PRECISION` | yes |  |  |
| `GR20` | `DOUBLE PRECISION` | yes |  |  |
| `GR21` | `DOUBLE PRECISION` | yes |  |  |
| `GR22` | `DOUBLE PRECISION` | yes |  |  |
| `GR23` | `DOUBLE PRECISION` | yes |  |  |
| `GR24` | `DOUBLE PRECISION` | yes |  |  |
| `GR25` | `DOUBLE PRECISION` | yes |  |  |
| `GR26` | `DOUBLE PRECISION` | yes |  |  |
| `GR27` | `DOUBLE PRECISION` | yes |  |  |
| `GR28` | `DOUBLE PRECISION` | yes |  |  |
| `GR29` | `DOUBLE PRECISION` | yes |  |  |
| `GR30` | `DOUBLE PRECISION` | yes |  |  |
| `GR31` | `DOUBLE PRECISION` | yes |  |  |
| `GR32` | `DOUBLE PRECISION` | yes |  |  |
| `GR33` | `DOUBLE PRECISION` | yes |  |  |
| `GR34` | `DOUBLE PRECISION` | yes |  |  |
| `GR35` | `DOUBLE PRECISION` | yes |  |  |
| `GR36` | `DOUBLE PRECISION` | yes |  |  |
| `GR37` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DATA_pk_idx` on `ID`, `ID_Form`, `ID_Section`, `ID_Row`
- `T_DATA_pkey` (primary, unique) on `Rec`

### Problems

- None

## year_2020.T_DIC_GROUP_INST

- Estimated rows: `15`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(255)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(50)` | yes |  |  |
| `Selected` | `BIT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_DIC_NAUKA

- Estimated rows: `643`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(20)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(4)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `TYPE` | `VARCHAR(510)` | yes |  |  |
| `Kod_Classifier` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_NAUKA_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2020.T_DIC_REPUBLIC

- Estimated rows: `241`
- Primary key: `KOD`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(12)` | no |  | PK, Indexed |
| `ID_Type` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `Sorting` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_REPUBLIC_pkey` (primary, unique) on `KOD`

### Problems

- None

## year_2020.T_DIC_SPEC

- Estimated rows: `1554`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(16)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(4)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `TYPE` | `VARCHAR(100)` | yes |  |  |
| `Kod_Classifier` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_SPEC_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2020.T_DIC_SPECIFIC

- Estimated rows: `7`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(50)` | yes |  |  |
| `NAME` | `VARCHAR(255)` | yes |  |  |
| `NAME_F` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_DIC_SPEC_CLOSED

- Estimated rows: `60`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_DIC_SPEC_SPECIFIC

- Estimated rows: `328`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(8)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(2)` | yes |  |  |
| `NAME` | `VARCHAR(255)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(255)` | yes |  |  |
| `TYPE` | `VARCHAR(50)` | yes |  |  |
| `Selected` | `BIT` | yes |  |  |
| `Specific` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_DIC_UGS

- Estimated rows: `87`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(510)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `ID_OTRASL` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_ERROR

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `Form_ID` | `INTEGER` | yes |  |  |
| `VO_ID` | `INTEGER` | yes |  |  |
| `Section_ID` | `INTEGER` | yes |  |  |
| `STRK` | `INTEGER` | yes |  |  |
| `DIC_VAL` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `ERR` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_FO

- Estimated rows: `8`
- Primary key: `NFO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `NFO` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_FO_pkey` (primary, unique) on `NFO`

### Problems

- None

## year_2020.T_Form_Cell

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `Dic_Source` | `VARCHAR(50)` | yes |  |  |
| `Format_Cell` | `VARCHAR(50)` | yes |  |  |
| `Default_Val` | `VARCHAR(50)` | yes |  |  |
| `Input_Type` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_Form_Col

- Estimated rows: `557`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Column_Num` | `INTEGER` | yes |  |  |
| `ID_Type_Col` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Width` | `INTEGER` | yes |  |  |
| `Field` | `VARCHAR(50)` | yes |  |  |
| `Alignment` | `VARCHAR(50)` | yes |  |  |
| `FieldType` | `VARCHAR(50)` | yes |  |  |
| `FieldDisplayFormat` | `VARCHAR(50)` | yes |  |  |
| `FieldEditFormat` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_Form_Col_Appendix

- Estimated rows: `59`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Column_Num` | `INTEGER` | yes |  |  |
| `ID_Type_Col` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Width` | `INTEGER` | yes |  |  |
| `Field` | `VARCHAR(50)` | yes |  |  |
| `Alignment` | `VARCHAR(50)` | yes |  |  |
| `FieldType` | `VARCHAR(50)` | yes |  |  |
| `FieldDisplayFormat` | `VARCHAR(50)` | yes |  |  |
| `FieldEditFormat` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_Form_Col_SumTotal

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_COL_NUM_DEST` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_CURRENT` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_PREV` | `VARCHAR(100)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_Form_Register

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Inst` | `INTEGER` | yes |  |  |
| `ID_User` | `INTEGER` | yes |  |  |
| `Form_Status` | `INTEGER` | yes |  |  |
| `DataStart` | `VARCHAR(50)` | yes |  |  |
| `DataEdit` | `VARCHAR(128)` | yes |  |  |
| `Version` | `VARCHAR(50)` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Check` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_Form_Row

- Estimated rows: `521`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `SECTION_TYPE` | `INTEGER` | yes |  |  |
| `ID_ROW_NUM` | `INTEGER` | yes |  |  |
| `ID_ROW_NUM_Display` | `VARCHAR(50)` | yes |  |  |
| `ID_TYPE_ROW` | `INTEGER` | yes |  |  |
| `NAME_ROW` | `VARCHAR(255)` | yes |  |  |
| `NAME_TAB_ROW` | `TEXT` | yes |  |  |
| `TOTAL_ROW` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_Form_Row_SumTotal

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_ROW_NUM_TOTAL` | `VARCHAR(50)` | yes |  |  |
| `ID_ROW_NUM_SUM` | `VARCHAR(100)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |
| `COL_NUM_TOTAL` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_Form_SumTotal

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_ROW_TOTAL` | `INTEGER` | yes |  |  |
| `ID_COL_NUM_DEST` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_CURRENT` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_PREV` | `VARCHAR(100)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_Forms

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `OKUD` | `VARCHAR(50)` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Short_Name` | `VARCHAR(255)` | yes |  |  |
| `Data_Start` | `VARCHAR(50)` | yes |  |  |
| `Version` | `VARCHAR(50)` | yes |  |  |
| `Order` | `VARCHAR(50)` | yes |  |  |
| `Order_orig` | `TEXT` | yes |  |  |
| `Status` | `BIT` | yes |  |  |
| `Year` | `INTEGER` | yes |  |  |
| `Selfname` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_INSTITUTION

- Estimated rows: `1214`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `Parent_ID` | `INTEGER` | yes |  |  |
| `pzk` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `ter` | `VARCHAR(10)` | yes |  |  |
| `Reg_Name` | `VARCHAR(100)` | yes |  |  |
| `ID_FO` | `INTEGER` | yes |  |  |
| `FO_Name` | `VARCHAR(100)` | yes |  |  |
| `ID_OKOGU` | `INTEGER` | yes |  |  |
| `OKOGU` | `VARCHAR(510)` | yes |  |  |
| `POST` | `VARCHAR(510)` | yes |  |  |
| `Website` | `VARCHAR(510)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_INSTITUTION_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2020.T_LIST_FIL

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `REC` | `INTEGER` | yes |  |  |
| `ID` | `INTEGER` | yes |  |  |
| `Name` | `TEXT` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |
| `OKATO` | `VARCHAR(50)` | yes |  |  |
| `OKSM` | `VARCHAR(50)` | yes |  |  |
| `KOD_EDU_PROG_1` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_2` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_3` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_4` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_5` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_6` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_7` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_8` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_9` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_10` | `BIT` | yes |  |  |
| `KOD_EDU_PROG_11` | `BIT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_LIST_UCH

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `REC` | `INTEGER` | yes |  |  |
| `ID` | `INTEGER` | yes |  |  |
| `Name` | `TEXT` | yes |  |  |
| `POST` | `VARCHAR(255)` | yes |  |  |
| `KOD_TEL` | `VARCHAR(50)` | yes |  |  |
| `TEL` | `VARCHAR(50)` | yes |  |  |
| `EMAIL` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_OU_SPECIFIC

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_OU` | `INTEGER` | yes |  |  |
| `NAME_OU` | `VARCHAR(255)` | yes |  |  |
| `KOD_SPECIFIC` | `INTEGER` | yes |  |  |
| `NAME_SPECIFIC` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_REGION

- Estimated rows: `103`
- Primary key: `TER`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `TER` | `VARCHAR(10)` | no |  | PK, Indexed |
| `ID_FO` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_REGION_pkey` (primary, unique) on `TER`

### Problems

- None

## year_2020.T_SECTION

- Estimated rows: `51`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(400)` | yes |  |  |
| `CAPTION` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_SECTION_Appendix

- Estimated rows: `13`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(200)` | yes |  |  |
| `CAPTION` | `VARCHAR(255)` | yes |  |  |
| `OKEI` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_SECTION_ERR

- Estimated rows: `52`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(200)` | yes |  |  |
| `NAME_SHORT` | `VARCHAR(50)` | yes |  |  |
| `CAPTION` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_TITUL_KAT

- Estimated rows: `3`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_TITUL_STATUS

- Estimated rows: `3`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_TITUL_TYPE

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_TITUL_VID

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_TYPE_DB

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `Type_DB` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_VERSION

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `Major_Version` | `INTEGER` | yes |  |  |
| `Minor_Version` | `INTEGER` | yes |  |  |
| `Release_Version` | `INTEGER` | yes |  |  |
| `Bulid_Version` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_VO

- Estimated rows: `5`
- Primary key: `VO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `VO` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(200)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_VO_pkey` (primary, unique) on `VO`

### Problems

- None

## year_2020.T_VO_N

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `VO` | `INTEGER` | yes |  |  |
| `VO_IBS` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(100)` | yes |  |  |
| `Selected` | `BIT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2020.T_YEAR

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_Cell_ReadOnly

- Estimated rows: `427`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `ID_Type_Cell` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_Cell_ReadOnly_MON

- Estimated rows: `1037`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `ID_Type_Cell` | `INTEGER` | yes |  |  |
| `Status_Cell` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_DATA

- Estimated rows: `872375`
- Primary key: `Rec`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `Rec` | `INTEGER` | no | `nextval('year_2021."T_DATA_Rec_seq"'::regclass)` | PK, Indexed |
| `ID` | `INTEGER` | yes |  | Indexed |
| `ID_Form` | `INTEGER` | yes |  | Indexed |
| `ID_Vo` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  | Indexed |
| `ID_Row` | `INTEGER` | yes |  | Indexed |
| `Dic_Val` | `INTEGER` | yes |  |  |
| `GR3` | `DOUBLE PRECISION` | yes |  |  |
| `GR4` | `DOUBLE PRECISION` | yes |  |  |
| `GR5` | `DOUBLE PRECISION` | yes |  |  |
| `GR6` | `DOUBLE PRECISION` | yes |  |  |
| `GR7` | `DOUBLE PRECISION` | yes |  |  |
| `GR8` | `DOUBLE PRECISION` | yes |  |  |
| `GR9` | `DOUBLE PRECISION` | yes |  |  |
| `GR10` | `DOUBLE PRECISION` | yes |  |  |
| `GR11` | `DOUBLE PRECISION` | yes |  |  |
| `GR12` | `DOUBLE PRECISION` | yes |  |  |
| `GR13` | `DOUBLE PRECISION` | yes |  |  |
| `GR14` | `DOUBLE PRECISION` | yes |  |  |
| `GR15` | `DOUBLE PRECISION` | yes |  |  |
| `GR16` | `DOUBLE PRECISION` | yes |  |  |
| `GR17` | `DOUBLE PRECISION` | yes |  |  |
| `GR18` | `DOUBLE PRECISION` | yes |  |  |
| `GR19` | `DOUBLE PRECISION` | yes |  |  |
| `GR20` | `DOUBLE PRECISION` | yes |  |  |
| `GR21` | `DOUBLE PRECISION` | yes |  |  |
| `GR22` | `DOUBLE PRECISION` | yes |  |  |
| `GR23` | `DOUBLE PRECISION` | yes |  |  |
| `GR24` | `DOUBLE PRECISION` | yes |  |  |
| `GR25` | `DOUBLE PRECISION` | yes |  |  |
| `GR26` | `DOUBLE PRECISION` | yes |  |  |
| `GR27` | `DOUBLE PRECISION` | yes |  |  |
| `GR28` | `DOUBLE PRECISION` | yes |  |  |
| `GR29` | `DOUBLE PRECISION` | yes |  |  |
| `GR30` | `DOUBLE PRECISION` | yes |  |  |
| `GR31` | `DOUBLE PRECISION` | yes |  |  |
| `GR32` | `DOUBLE PRECISION` | yes |  |  |
| `GR33` | `DOUBLE PRECISION` | yes |  |  |
| `GR34` | `DOUBLE PRECISION` | yes |  |  |
| `GR35` | `DOUBLE PRECISION` | yes |  |  |
| `GR36` | `DOUBLE PRECISION` | yes |  |  |
| `GR37` | `DOUBLE PRECISION` | yes |  |  |
| `GR38` | `DOUBLE PRECISION` | yes |  |  |
| `GR39` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DATA_pk_idx` on `ID`, `ID_Form`, `ID_Section`, `ID_Row`
- `T_DATA_pkey` (primary, unique) on `Rec`

### Problems

- None

## year_2021.T_DIC_GROUP_INST

- Estimated rows: `15`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(255)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(50)` | yes |  |  |
| `Selected` | `BIT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_DIC_NAUKA

- Estimated rows: `987`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(20)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(4)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `TYPE` | `VARCHAR(510)` | yes |  |  |
| `Kod_Classifier` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_NAUKA_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2021.T_DIC_REPUBLIC

- Estimated rows: `241`
- Primary key: `KOD`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(12)` | no |  | PK, Indexed |
| `ID_Type` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `Sorting` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_REPUBLIC_pkey` (primary, unique) on `KOD`

### Problems

- None

## year_2021.T_DIC_SPEC

- Estimated rows: `1596`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(16)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(4)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `TYPE` | `VARCHAR(100)` | yes |  |  |
| `Kod_Classifier` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_SPEC_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2021.T_DIC_SPECIFIC

- Estimated rows: `7`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(50)` | yes |  |  |
| `NAME` | `VARCHAR(255)` | yes |  |  |
| `NAME_F` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_DIC_SPEC_CLOSED

- Estimated rows: `60`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_DIC_SPEC_SPECIFIC

- Estimated rows: `328`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(8)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(2)` | yes |  |  |
| `NAME` | `VARCHAR(255)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(255)` | yes |  |  |
| `TYPE` | `VARCHAR(50)` | yes |  |  |
| `Selected` | `BIT` | yes |  |  |
| `Specific` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_DIC_UGS

- Estimated rows: `87`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(510)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `ID_OTRASL` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_ERROR

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `Form_ID` | `INTEGER` | yes |  |  |
| `VO_ID` | `INTEGER` | yes |  |  |
| `Section_ID` | `INTEGER` | yes |  |  |
| `STRK` | `INTEGER` | yes |  |  |
| `DIC_VAL` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `ERR` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_FO

- Estimated rows: `8`
- Primary key: `NFO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `NFO` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(100)` | yes |  |  |
| `K` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_FO_pkey` (primary, unique) on `NFO`

### Problems

- None

## year_2021.T_Form_Cell

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `Dic_Source` | `VARCHAR(50)` | yes |  |  |
| `Format_Cell` | `VARCHAR(50)` | yes |  |  |
| `Default_Val` | `VARCHAR(50)` | yes |  |  |
| `Input_Type` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_Form_Col

- Estimated rows: `569`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Column_Num` | `INTEGER` | yes |  |  |
| `ID_Type_Col` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Width` | `INTEGER` | yes |  |  |
| `Field` | `VARCHAR(50)` | yes |  |  |
| `Alignment` | `VARCHAR(50)` | yes |  |  |
| `FieldType` | `VARCHAR(50)` | yes |  |  |
| `FieldDisplayFormat` | `VARCHAR(50)` | yes |  |  |
| `FieldEditFormat` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_Form_Col_Appendix

- Estimated rows: `65`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Column_Num` | `INTEGER` | yes |  |  |
| `ID_Type_Col` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Width` | `INTEGER` | yes |  |  |
| `Field` | `VARCHAR(50)` | yes |  |  |
| `Alignment` | `VARCHAR(50)` | yes |  |  |
| `FieldType` | `VARCHAR(50)` | yes |  |  |
| `FieldDisplayFormat` | `VARCHAR(50)` | yes |  |  |
| `FieldEditFormat` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_Form_Col_SumTotal

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_COL_NUM_DEST` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_CURRENT` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_PREV` | `VARCHAR(100)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_Form_Register

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Inst` | `INTEGER` | yes |  |  |
| `ID_User` | `INTEGER` | yes |  |  |
| `Form_Status` | `INTEGER` | yes |  |  |
| `DataStart` | `VARCHAR(50)` | yes |  |  |
| `DataEdit` | `VARCHAR(128)` | yes |  |  |
| `Version` | `VARCHAR(50)` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Check` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_Form_Row

- Estimated rows: `537`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `SECTION_TYPE` | `INTEGER` | yes |  |  |
| `ID_ROW_NUM` | `INTEGER` | yes |  |  |
| `ID_ROW_NUM_Display` | `VARCHAR(50)` | yes |  |  |
| `ID_TYPE_ROW` | `INTEGER` | yes |  |  |
| `NAME_ROW` | `VARCHAR(255)` | yes |  |  |
| `NAME_TAB_ROW` | `TEXT` | yes |  |  |
| `TOTAL_ROW` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_Form_Row_SumTotal

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_ROW_NUM_TOTAL` | `VARCHAR(50)` | yes |  |  |
| `ID_ROW_NUM_SUM` | `VARCHAR(100)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |
| `COL_NUM_TOTAL` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_Form_SumTotal

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_ROW_TOTAL` | `INTEGER` | yes |  |  |
| `ID_COL_NUM_DEST` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_CURRENT` | `VARCHAR(50)` | yes |  |  |
| `ID_COL_NUM_PREV` | `VARCHAR(100)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_Forms

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `OKUD` | `VARCHAR(50)` | yes |  |  |
| `Name` | `VARCHAR(255)` | yes |  |  |
| `Short_Name` | `VARCHAR(255)` | yes |  |  |
| `Data_Start` | `VARCHAR(50)` | yes |  |  |
| `Version` | `VARCHAR(50)` | yes |  |  |
| `Order` | `VARCHAR(50)` | yes |  |  |
| `Order_orig` | `TEXT` | yes |  |  |
| `Status` | `BIT` | yes |  |  |
| `Year` | `INTEGER` | yes |  |  |
| `Selfname` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_INSTITUTION

- Estimated rows: `1136`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `Parent_ID` | `INTEGER` | yes |  |  |
| `pzk` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `TER` | `INTEGER` | yes |  |  |
| `Reg_Name` | `VARCHAR(100)` | yes |  |  |
| `ID_FO` | `INTEGER` | yes |  |  |
| `FO_Name` | `VARCHAR(100)` | yes |  |  |
| `ID_OKOGU` | `INTEGER` | yes |  |  |
| `OKOGU` | `VARCHAR(510)` | yes |  |  |
| `POST` | `VARCHAR(510)` | yes |  |  |
| `Website` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_INSTITUTION_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2021.T_LIST_UCH

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `REC` | `INTEGER` | yes |  |  |
| `ID` | `INTEGER` | yes |  |  |
| `Name` | `TEXT` | yes |  |  |
| `POST` | `VARCHAR(255)` | yes |  |  |
| `KOD_TEL` | `VARCHAR(50)` | yes |  |  |
| `TEL` | `VARCHAR(50)` | yes |  |  |
| `EMAIL` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_OU_SPECIFIC

- Estimated rows: `2`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_OU` | `INTEGER` | yes |  |  |
| `NAME_OU` | `VARCHAR(255)` | yes |  |  |
| `KOD_SPECIFIC` | `INTEGER` | yes |  |  |
| `NAME_SPECIFIC` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_REGION

- Estimated rows: `103`
- Primary key: `TER`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `TER` | `INTEGER` | no |  | PK, Indexed |
| `ID_FO` | `INTEGER` | yes |  |  |
| `ER` | `VARCHAR(6)` | yes |  |  |
| `Name` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_REGION_pkey` (primary, unique) on `TER`

### Problems

- None

## year_2021.T_SECTION

- Estimated rows: `51`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(400)` | yes |  |  |
| `CAPTION` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_SECTION_Appendix

- Estimated rows: `15`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(200)` | yes |  |  |
| `CAPTION` | `VARCHAR(255)` | yes |  |  |
| `OKEI` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_SECTION_ERR

- Estimated rows: `52`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(200)` | yes |  |  |
| `NAME_SHORT` | `VARCHAR(50)` | yes |  |  |
| `CAPTION` | `VARCHAR(255)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_TITUL_KAT

- Estimated rows: `3`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_TITUL_STATUS

- Estimated rows: `3`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_TITUL_TYPE

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_TITUL_VID

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(50)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_TYPE_DB

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `Type_DB` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_VERSION

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `Major_Version` | `INTEGER` | yes |  |  |
| `Minor_Version` | `INTEGER` | yes |  |  |
| `Release_Version` | `INTEGER` | yes |  |  |
| `Bulid_Version` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_VO

- Estimated rows: `5`
- Primary key: `VO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `VO` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(200)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_VO_pkey` (primary, unique) on `VO`

### Problems

- None

## year_2021.T_VO_N

- Estimated rows: `5`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `VO` | `INTEGER` | yes |  |  |
| `VO_IBS` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(100)` | yes |  |  |
| `Selected` | `BIT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2021.T_YEAR

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2022.T_Cell_ReadOnly

- Estimated rows: `420`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no | `nextval('year_2022."T_Cell_ReadOnly_ID_seq"'::regclass)` |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `ID_Type_Cell` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2022.T_Cell_ReadOnly_MON

- Estimated rows: `1049`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no | `nextval('year_2022."T_Cell_ReadOnly_MON_ID_seq"'::regclass)` |  |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `ID_Type_Cell` | `INTEGER` | yes |  |  |
| `Status_Cell` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2022.T_DATA

- Estimated rows: `881371`
- Primary key: `Rec`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `Rec` | `INTEGER` | no | `nextval('year_2022."T_DATA_Rec_seq"'::regclass)` | PK, Indexed |
| `ID` | `INTEGER` | yes |  | Indexed |
| `ID_Form` | `INTEGER` | yes |  | Indexed |
| `ID_Vo` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  | Indexed |
| `ID_Row` | `INTEGER` | yes |  | Indexed |
| `Dic_Val` | `INTEGER` | yes |  |  |
| `GR3` | `DOUBLE PRECISION` | yes |  |  |
| `GR4` | `DOUBLE PRECISION` | yes |  |  |
| `GR5` | `DOUBLE PRECISION` | yes |  |  |
| `GR6` | `DOUBLE PRECISION` | yes |  |  |
| `GR7` | `DOUBLE PRECISION` | yes |  |  |
| `GR8` | `DOUBLE PRECISION` | yes |  |  |
| `GR9` | `DOUBLE PRECISION` | yes |  |  |
| `GR10` | `DOUBLE PRECISION` | yes |  |  |
| `GR11` | `DOUBLE PRECISION` | yes |  |  |
| `GR12` | `DOUBLE PRECISION` | yes |  |  |
| `GR13` | `DOUBLE PRECISION` | yes |  |  |
| `GR14` | `DOUBLE PRECISION` | yes |  |  |
| `GR15` | `DOUBLE PRECISION` | yes |  |  |
| `GR16` | `DOUBLE PRECISION` | yes |  |  |
| `GR17` | `DOUBLE PRECISION` | yes |  |  |
| `GR18` | `DOUBLE PRECISION` | yes |  |  |
| `GR19` | `DOUBLE PRECISION` | yes |  |  |
| `GR20` | `DOUBLE PRECISION` | yes |  |  |
| `GR21` | `DOUBLE PRECISION` | yes |  |  |
| `GR22` | `DOUBLE PRECISION` | yes |  |  |
| `GR23` | `DOUBLE PRECISION` | yes |  |  |
| `GR24` | `DOUBLE PRECISION` | yes |  |  |
| `GR25` | `DOUBLE PRECISION` | yes |  |  |
| `GR26` | `DOUBLE PRECISION` | yes |  |  |
| `GR27` | `DOUBLE PRECISION` | yes |  |  |
| `GR28` | `DOUBLE PRECISION` | yes |  |  |
| `GR29` | `DOUBLE PRECISION` | yes |  |  |
| `GR30` | `DOUBLE PRECISION` | yes |  |  |
| `GR31` | `DOUBLE PRECISION` | yes |  |  |
| `GR32` | `DOUBLE PRECISION` | yes |  |  |
| `GR33` | `DOUBLE PRECISION` | yes |  |  |
| `GR34` | `DOUBLE PRECISION` | yes |  |  |
| `GR35` | `DOUBLE PRECISION` | yes |  |  |
| `GR36` | `DOUBLE PRECISION` | yes |  |  |
| `GR37` | `DOUBLE PRECISION` | yes |  |  |
| `GR38` | `DOUBLE PRECISION` | yes |  |  |
| `GR39` | `DOUBLE PRECISION` | yes |  |  |
| `GR40` | `DOUBLE PRECISION` | yes |  |  |
| `GR41` | `DOUBLE PRECISION` | yes |  |  |
| `GR42` | `DOUBLE PRECISION` | yes |  |  |
| `GR43` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DATA_pk_idx` on `ID`, `ID_Form`, `ID_Section`, `ID_Row`
- `T_DATA_pkey` (primary, unique) on `Rec`

### Problems

- None

## year_2022.T_DIC_GROUP_INST

- Estimated rows: `15`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(100)` | yes |  |  |
| `Selected` | `INTEGER` | no |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2022.T_DIC_NAUKA

- Estimated rows: `924`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(20)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(4)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `TYPE` | `VARCHAR(510)` | yes |  |  |
| `Kod_Classifier` | `INTEGER` | yes |  |  |
| `Selected` | `BOOLEAN` | no |  |  |
| `KOD_pr59` | `VARCHAR(510)` | yes |  |  |
| `NAME_pr59` | `VARCHAR(510)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_NAUKA_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2022.T_DIC_REPUBLIC

- Estimated rows: `243`
- Primary key: `KOD`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(12)` | no |  | PK, Indexed |
| `ID_Type` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `Sorting` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_REPUBLIC_pkey` (primary, unique) on `KOD`

### Problems

- None

## year_2022.T_DIC_SPEC

- Estimated rows: `1596`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(16)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(4)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  | Indexed |
| `TYPE` | `VARCHAR(100)` | yes |  |  |
| `Kod_Classifier` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_SPEC_KOD_NAME_idx` on `KOD_NAME`
- `T_DIC_SPEC_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2022.T_DIC_SPECIFIC

- Estimated rows: `7`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(100)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `NAME_F` | `VARCHAR(510)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_SPECIFIC_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2022.T_DIC_SPEC_CLOSED

- Estimated rows: `60`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |

### Foreign Keys

- None

### Indexes

- `T_DIC_SPEC_CLOSED_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2022.T_DIC_SPEC_SPECIFIC

- Estimated rows: `328`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(16)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(4)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `TYPE` | `VARCHAR(100)` | yes |  |  |
| `Selected` | `INTEGER` | no |  |  |
| `Specific` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_SPEC_SPECIFIC_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2022.T_DIC_UGS

- Estimated rows: `87`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(510)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `ID_OTRASL` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2022.T_ERROR

- Estimated rows: `0`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `Form_ID` | `INTEGER` | yes |  |  |
| `VO_ID` | `INTEGER` | yes |  |  |
| `Section_ID` | `INTEGER` | yes |  |  |
| `STRK` | `INTEGER` | yes |  |  |
| `DIC_VAL` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `ERR` | `VARCHAR(510)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2022.T_FO

- Estimated rows: `8`
- Primary key: `NFO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `NFO` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_FO_pkey` (primary, unique) on `NFO`

### Problems

- None

## year_2022.T_Form_Cell

- Estimated rows: `0`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `ID_Col` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `Dic_Source` | `VARCHAR(100)` | yes |  |  |
| `Format_Cell` | `VARCHAR(100)` | yes |  |  |
| `Default_Val` | `VARCHAR(100)` | yes |  |  |
| `Input_Type` | `SMALLINT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_Form_Cell_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_Form_Col

- Estimated rows: `578`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no | `nextval('year_2022."T_Form_Col_ID_seq"'::regclass)` | PK, Indexed |
| `ID_Form` | `INTEGER` | yes |  | Indexed |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Column_Num` | `INTEGER` | yes |  |  |
| `ID_Type_Col` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `Width` | `INTEGER` | yes |  |  |
| `Field` | `VARCHAR(100)` | yes |  |  |
| `Alignment` | `VARCHAR(100)` | yes |  |  |
| `FieldType` | `VARCHAR(100)` | yes |  |  |
| `FieldDisplayFormat` | `VARCHAR(100)` | yes |  |  |
| `FieldEditFormat` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_Form_Col_T_Form_ColID_FORM_idx` on `ID_Form`
- `T_Form_Col_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_Form_Col_Appendix

- Estimated rows: `65`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no | `nextval('year_2022."T_Form_Col_Appendix_ID_seq"'::regclass)` | PK, Indexed |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Column_Num` | `INTEGER` | yes |  |  |
| `ID_Type_Col` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `Width` | `INTEGER` | yes |  |  |
| `Field` | `VARCHAR(100)` | yes |  |  |
| `Alignment` | `VARCHAR(100)` | yes |  |  |
| `FieldType` | `VARCHAR(100)` | yes |  |  |
| `FieldDisplayFormat` | `VARCHAR(100)` | yes |  |  |
| `FieldEditFormat` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_Form_Col_Appendix_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_Form_Col_SumTotal

- Estimated rows: `0`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no | `nextval('year_2022."T_Form_Col_SumTotal_ID_seq"'::regclass)` | PK, Indexed |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_COL_NUM_DEST` | `VARCHAR(100)` | yes |  | Indexed |
| `ID_COL_NUM_CURRENT` | `VARCHAR(100)` | yes |  | Indexed |
| `ID_COL_NUM_PREV` | `VARCHAR(200)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_Form_Col_SumTotal_ID_COL_NUM_CURRENT_idx` on `ID_COL_NUM_DEST`
- `T_Form_Col_SumTotal_T_FORM_ROWID_Row_idx` on `ID_COL_NUM_CURRENT`
- `T_Form_Col_SumTotal_T_FORM_ROWID_idx` on `ID`
- `T_Form_Col_SumTotal_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_Form_Register

- Estimated rows: `0`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no | `nextval('year_2022."T_Form_Register_ID_seq"'::regclass)` | PK, Indexed |
| `ID_Form` | `INTEGER` | yes |  |  |
| `ID_Inst` | `INTEGER` | yes |  |  |
| `ID_User` | `INTEGER` | yes |  |  |
| `Form_Status` | `INTEGER` | yes |  |  |
| `DataStart` | `VARCHAR(100)` | yes |  |  |
| `DataEdit` | `TIMESTAMP` | yes |  |  |
| `Version` | `VARCHAR(100)` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `Check` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_Form_Register_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_Form_Row

- Estimated rows: `537`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no | `nextval('year_2022."T_Form_Row_ID_seq"'::regclass)` | PK, Indexed |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `SECTION_TYPE` | `INTEGER` | yes |  |  |
| `ID_ROW_NUM` | `INTEGER` | yes |  | Indexed |
| `ID_ROW_NUM_Display` | `VARCHAR(100)` | yes |  |  |
| `ID_TYPE_ROW` | `INTEGER` | yes |  |  |
| `NAME_ROW` | `VARCHAR(510)` | yes |  |  |
| `NAME_TAB_ROW` | `TEXT` | yes |  |  |
| `TOTAL_ROW` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_Form_Row_T_FORM_ROWID_Row_idx` on `ID_ROW_NUM`
- `T_Form_Row_T_FORM_ROWID_idx` on `ID`
- `T_Form_Row_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_Form_Row_SumTotal

- Estimated rows: `0`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no | `nextval('year_2022."T_Form_Row_SumTotal_ID_seq"'::regclass)` | PK, Indexed |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_ROW_NUM_TOTAL` | `VARCHAR(100)` | yes |  | Indexed |
| `ID_ROW_NUM_SUM` | `VARCHAR(200)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |
| `COL_NUM_TOTAL` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_Form_Row_SumTotal_T_FORM_ROWID_Row_idx` on `ID_ROW_NUM_TOTAL`
- `T_Form_Row_SumTotal_T_FORM_ROWID_idx` on `ID`
- `T_Form_Row_SumTotal_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_Form_SumTotal

- Estimated rows: `0`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no | `nextval('year_2022."T_Form_SumTotal_ID_seq"'::regclass)` | PK, Indexed |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_ROW_TOTAL` | `INTEGER` | yes |  |  |
| `ID_COL_NUM_DEST` | `VARCHAR(100)` | yes |  | Indexed |
| `ID_COL_NUM_CURRENT` | `VARCHAR(100)` | yes |  | Indexed |
| `ID_COL_NUM_PREV` | `VARCHAR(200)` | yes |  |  |
| `PRIORITY` | `INTEGER` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_Form_SumTotal_ID_COL_NUM_CURRENT_idx` on `ID_COL_NUM_DEST`
- `T_Form_SumTotal_T_FORM_ROWID_Row_idx` on `ID_COL_NUM_CURRENT`
- `T_Form_SumTotal_T_FORM_ROWID_idx` on `ID`
- `T_Form_SumTotal_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_Forms

- Estimated rows: `1`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `OKUD` | `VARCHAR(100)` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `Short_Name` | `VARCHAR(510)` | yes |  |  |
| `Data_Start` | `VARCHAR(100)` | yes |  |  |
| `Version` | `VARCHAR(100)` | yes |  |  |
| `Order` | `VARCHAR(100)` | yes |  |  |
| `Order_orig` | `BYTEA` | yes |  |  |
| `Status` | `INTEGER` | no |  |  |
| `Year` | `INTEGER` | yes |  |  |
| `Selfname` | `VARCHAR(510)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_Forms_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_INSTITUTION

- Estimated rows: `1166`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `Parent_ID` | `INTEGER` | yes |  |  |
| `pzk` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `TER` | `INTEGER` | yes |  |  |
| `Reg_Name` | `VARCHAR(100)` | yes |  |  |
| `ID_FO` | `INTEGER` | yes |  |  |
| `FO_Name` | `VARCHAR(100)` | yes |  |  |
| `ID_OKOGU` | `INTEGER` | yes |  |  |
| `OKOGU` | `VARCHAR(510)` | yes |  |  |
| `POST` | `VARCHAR(510)` | yes |  |  |
| `Website` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_INSTITUTION_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_LIST_FIL

- Estimated rows: `0`
- Primary key: `REC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `REC` | `INTEGER` | no | `nextval('year_2022."T_LIST_FIL_REC_seq"'::regclass)` | PK, Indexed |
| `ID` | `INTEGER` | yes |  |  |
| `Name` | `TEXT` | yes |  |  |
| `TYPE` | `INTEGER` | yes |  |  |
| `OKATO` | `VARCHAR(100)` | yes |  |  |
| `OKSM` | `VARCHAR(100)` | yes |  |  |
| `KOD_EDU_PROG_1` | `INTEGER` | no |  |  |
| `KOD_EDU_PROG_2` | `INTEGER` | no |  |  |
| `KOD_EDU_PROG_3` | `INTEGER` | no |  |  |
| `KOD_EDU_PROG_4` | `INTEGER` | no |  |  |
| `KOD_EDU_PROG_5` | `INTEGER` | no |  |  |
| `KOD_EDU_PROG_6` | `INTEGER` | no |  |  |
| `KOD_EDU_PROG_7` | `INTEGER` | no |  |  |
| `KOD_EDU_PROG_8` | `INTEGER` | no |  |  |
| `KOD_EDU_PROG_9` | `INTEGER` | no |  |  |
| `KOD_EDU_PROG_10` | `INTEGER` | no |  |  |
| `KOD_EDU_PROG_11` | `INTEGER` | no |  |  |
| `POK_1` | `INTEGER` | yes |  |  |
| `POK_2` | `INTEGER` | yes |  |  |
| `POK_3` | `INTEGER` | yes |  |  |
| `POK_4` | `DOUBLE PRECISION` | yes |  |  |
| `POK_5` | `DOUBLE PRECISION` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_LIST_FIL_pkey` (primary, unique) on `REC`

### Problems

- None

## year_2022.T_LIST_UCH

- Estimated rows: `0`
- Primary key: `REC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `REC` | `INTEGER` | no | `nextval('year_2022."T_LIST_UCH_REC_seq"'::regclass)` | PK, Indexed |
| `ID` | `INTEGER` | yes |  |  |
| `Name` | `TEXT` | yes |  |  |
| `POST` | `VARCHAR(510)` | yes |  |  |
| `KOD_TEL` | `VARCHAR(100)` | yes |  |  |
| `TEL` | `VARCHAR(100)` | yes |  |  |
| `EMAIL` | `VARCHAR(510)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_LIST_UCH_pkey` (primary, unique) on `REC`

### Problems

- None

## year_2022.T_OU_SPECIFIC

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_OU` | `INTEGER` | yes |  |  |
| `NAME_OU` | `VARCHAR(510)` | yes |  |  |
| `KOD_SPECIFIC` | `INTEGER` | yes |  |  |
| `NAME_SPECIFIC` | `VARCHAR(510)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2022.T_REGION

- Estimated rows: `103`
- Primary key: `TER`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `TER` | `INTEGER` | no |  | PK, Indexed |
| `ID_FO` | `INTEGER` | yes |  |  |
| `ER` | `VARCHAR(6)` | yes |  |  |
| `Name` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_REGION_pkey` (primary, unique) on `TER`

### Problems

- None

## year_2022.T_SECTION

- Estimated rows: `51`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(400)` | yes |  |  |
| `CAPTION` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2022.T_SECTION_Appendix

- Estimated rows: `15`
- Primary key: `ID_FORM, ID_SECTION`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | no |  | PK, Indexed |
| `ID_SECTION` | `INTEGER` | no |  | PK, Indexed |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(400)` | yes |  |  |
| `CAPTION` | `VARCHAR(510)` | yes |  |  |
| `OKEI` | `VARCHAR(510)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_SECTION_Appendix_pkey` (primary, unique) on `ID_FORM`, `ID_SECTION`

### Problems

- None

## year_2022.T_SECTION_ERR

- Estimated rows: `52`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_FORM` | `INTEGER` | yes |  |  |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `ID_TYPE` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(400)` | yes |  |  |
| `NAME_SHORT` | `VARCHAR(100)` | yes |  |  |
| `CAPTION` | `VARCHAR(510)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2022.T_TITUL_KAT

- Estimated rows: `3`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_TITUL_KAT_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_TITUL_STATUS

- Estimated rows: `3`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_TITUL_STATUS_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_TITUL_TYPE

- Estimated rows: `5`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_TITUL_TYPE_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_TITUL_VID

- Estimated rows: `5`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_TITUL_VID_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_TYPE_DB

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `Type_DB` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2022.T_VERSION

- Estimated rows: `1`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `Major_Version` | `INTEGER` | yes |  |  |
| `Minor_Version` | `INTEGER` | yes |  |  |
| `Release_Version` | `INTEGER` | yes |  |  |
| `Bulid_Version` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_VERSION_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2022.T_VO

- Estimated rows: `5`
- Primary key: `VO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `VO` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(200)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_VO_pkey` (primary, unique) on `VO`

### Problems

- None

## year_2022.T_VO_N

- Estimated rows: `5`
- Primary key: `VO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `VO` | `INTEGER` | no |  | PK, Indexed |
| `VO_IBS` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(200)` | yes |  |  |
| `Selected` | `INTEGER` | no |  |  |

### Foreign Keys

- None

### Indexes

- `T_VO_N_pkey` (primary, unique) on `VO`

### Problems

- None

## year_2022.T_YEAR

- Estimated rows: `1`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2022.dbo_T_Institute_vpo

- Estimated rows: `14051`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Parent` | `INTEGER` | yes |  |  |
| `ID_CITIS` | `INTEGER` | yes |  |  |
| `NAME` | `TEXT` | yes |  |  |
| `inst_destroy` | `INTEGER` | yes |  |  |
| `OKOGU` | `INTEGER` | yes |  |  |
| `OKOGU_new` | `INTEGER` | yes |  |  |
| `OKPO` | `VARCHAR(510)` | yes |  |  |
| `TER` | `VARCHAR(30)` | yes |  |  |
| `POST` | `VARCHAR(510)` | yes |  |  |
| `Leader_Fio` | `VARCHAR(510)` | yes |  |  |
| `Leader_Tel` | `VARCHAR(510)` | yes |  |  |
| `Website` | `VARCHAR(510)` | yes |  |  |
| `Email` | `VARCHAR(510)` | yes |  |  |
| `INN` | `VARCHAR(100)` | yes |  |  |
| `comment` | `VARCHAR(510)` | yes |  |  |
| `org_type` | `VARCHAR(100)` | yes |  |  |
| `field1` | `VARCHAR(510)` | yes |  |  |
| `key_gzgu` | `VARCHAR(510)` | yes |  |  |
| `koordinats` | `VARCHAR(510)` | yes |  |  |
| `ident` | `INTEGER` | no | `nextval('year_2022."dbo_T_Institute_vpo_ident_seq"'::regclass)` |  |
| `EmailMonitoring` | `VARCHAR(510)` | yes |  |  |
| `town` | `VARCHAR(300)` | yes |  |  |
| `date` | `VARCHAR(300)` | yes |  |  |
| `ogrn` | `VARCHAR(40)` | yes |  |  |
| `kpp` | `VARCHAR(40)` | yes |  |  |
| `name_full` | `TEXT` | yes |  |  |
| `checked` | `INTEGER` | yes |  |  |
| `selected` | `BOOLEAN` | no |  |  |
| `education_programms` | `VARCHAR(20)` | yes |  |  |
| `type_org` | `VARCHAR(100)` | yes |  |  |
| `priznak` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2023.T_DATA

- Estimated rows: `945943`
- Primary key: `idx`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | yes |  |  |
| `ID_Vo` | `INTEGER` | yes |  |  |
| `ID_Section` | `INTEGER` | yes |  |  |
| `ID_Row` | `INTEGER` | yes |  |  |
| `Dic_Val` | `INTEGER` | yes |  |  |
| `GR3` | `DOUBLE PRECISION` | yes |  |  |
| `GR4` | `DOUBLE PRECISION` | yes |  |  |
| `GR5` | `DOUBLE PRECISION` | yes |  |  |
| `GR6` | `DOUBLE PRECISION` | yes |  |  |
| `GR7` | `DOUBLE PRECISION` | yes |  |  |
| `GR8` | `DOUBLE PRECISION` | yes |  |  |
| `GR9` | `DOUBLE PRECISION` | yes |  |  |
| `GR10` | `DOUBLE PRECISION` | yes |  |  |
| `GR11` | `DOUBLE PRECISION` | yes |  |  |
| `GR12` | `DOUBLE PRECISION` | yes |  |  |
| `GR13` | `DOUBLE PRECISION` | yes |  |  |
| `GR14` | `DOUBLE PRECISION` | yes |  |  |
| `GR15` | `DOUBLE PRECISION` | yes |  |  |
| `GR16` | `DOUBLE PRECISION` | yes |  |  |
| `GR17` | `DOUBLE PRECISION` | yes |  |  |
| `GR18` | `DOUBLE PRECISION` | yes |  |  |
| `GR19` | `DOUBLE PRECISION` | yes |  |  |
| `GR20` | `DOUBLE PRECISION` | yes |  |  |
| `GR21` | `DOUBLE PRECISION` | yes |  |  |
| `GR22` | `DOUBLE PRECISION` | yes |  |  |
| `GR23` | `DOUBLE PRECISION` | yes |  |  |
| `GR24` | `DOUBLE PRECISION` | yes |  |  |
| `GR25` | `DOUBLE PRECISION` | yes |  |  |
| `GR26` | `DOUBLE PRECISION` | yes |  |  |
| `GR27` | `DOUBLE PRECISION` | yes |  |  |
| `GR28` | `DOUBLE PRECISION` | yes |  |  |
| `GR29` | `DOUBLE PRECISION` | yes |  |  |
| `GR30` | `DOUBLE PRECISION` | yes |  |  |
| `GR31` | `DOUBLE PRECISION` | yes |  |  |
| `GR32` | `DOUBLE PRECISION` | yes |  |  |
| `GR33` | `DOUBLE PRECISION` | yes |  |  |
| `GR34` | `DOUBLE PRECISION` | yes |  |  |
| `GR35` | `DOUBLE PRECISION` | yes |  |  |
| `GR36` | `DOUBLE PRECISION` | yes |  |  |
| `GR37` | `DOUBLE PRECISION` | yes |  |  |
| `GR38` | `DOUBLE PRECISION` | yes |  |  |
| `GR39` | `DOUBLE PRECISION` | yes |  |  |
| `GR40` | `DOUBLE PRECISION` | yes |  |  |
| `GR41` | `DOUBLE PRECISION` | yes |  |  |
| `GR42` | `DOUBLE PRECISION` | yes |  |  |
| `GR43` | `TEXT` | yes |  |  |
| `update_datetime` | `TIMESTAMP` | yes |  |  |
| `idx` | `VARCHAR(510)` | no |  | PK, Indexed |
| `Rec` | `INTEGER` | yes | `nextval('year_2023."T_DATA_Rec_seq"'::regclass)` |  |

### Foreign Keys

- None

### Indexes

- `T_DATA_pkey` (primary, unique) on `idx`

### Problems

- None

## year_2023.T_DIC_NAUKA

- Estimated rows: `1002`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(20)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |
| `TYPE` | `VARCHAR(510)` | yes |  |  |
| `Kod_Classifier` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_NAUKA_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2023.T_DIC_REPUBLIC

- Estimated rows: `243`
- Primary key: `KOD`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(12)` | no |  | PK, Indexed |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_REPUBLIC_pkey` (primary, unique) on `KOD`

### Problems

- None

## year_2023.T_DIC_SPEC

- Estimated rows: `1776`
- Primary key: `ID_DIC`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | no |  | PK, Indexed |
| `KOD` | `VARCHAR(16)` | yes |  |  |
| `Kod_Kval` | `VARCHAR(4)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |
| `KOD_NAME` | `VARCHAR(510)` | yes |  | Indexed |
| `TYPE` | `VARCHAR(100)` | yes |  |  |
| `Kod_Classifier` | `INTEGER` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_DIC_SPEC_KOD_NAME_idx` on `KOD_NAME`
- `T_DIC_SPEC_pkey` (primary, unique) on `ID_DIC`

### Problems

- None

## year_2023.T_DIC_UGS

- Estimated rows: `87`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_DIC` | `INTEGER` | yes |  |  |
| `KOD` | `VARCHAR(510)` | yes |  |  |
| `NAME` | `VARCHAR(510)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2023.T_FO

- Estimated rows: `0`
- Primary key: `NFO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `NFO` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_FO_pkey` (primary, unique) on `NFO`

### Problems

- None

## year_2023.T_INSTITUTION

- Estimated rows: `1234`
- Primary key: `ID`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID` | `INTEGER` | no |  | PK, Indexed |
| `Parent_ID` | `INTEGER` | yes |  |  |
| `pzk` | `INTEGER` | yes |  |  |
| `Name` | `VARCHAR(510)` | yes |  |  |
| `TER` | `INTEGER` | yes |  |  |
| `Reg_Name` | `VARCHAR(100)` | yes |  |  |
| `ID_FO` | `INTEGER` | yes |  |  |
| `FO_Name` | `VARCHAR(100)` | yes |  |  |
| `ID_OKOGU` | `INTEGER` | yes |  |  |
| `OKOGU` | `VARCHAR(510)` | yes |  |  |
| `POST` | `VARCHAR(510)` | yes |  |  |
| `Website` | `VARCHAR(510)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_INSTITUTION_pkey` (primary, unique) on `ID`

### Problems

- None

## year_2023.T_REGION

- Estimated rows: `90`
- Primary key: `TER`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `TER` | `INTEGER` | no |  | PK, Indexed |
| `Name` | `VARCHAR(100)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_REGION_pkey` (primary, unique) on `TER`

### Problems

- None

## year_2023.T_SECTION

- Estimated rows: `51`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `ID_SECTION` | `INTEGER` | yes |  |  |
| `NAME` | `VARCHAR(400)` | yes |  |  |
| `NAME_SHORT` | `VARCHAR(100)` | yes |  |  |
| `CAPTION` | `TEXT` | yes |  |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.

## year_2023.T_VO

- Estimated rows: `0`
- Primary key: `VO`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `VO` | `INTEGER` | no |  | PK, Indexed |
| `NAME` | `VARCHAR(200)` | yes |  |  |

### Foreign Keys

- None

### Indexes

- `T_VO_pkey` (primary, unique) on `VO`

### Problems

- None
