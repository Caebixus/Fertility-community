from django.urls import path

from . import views

urlpatterns = [
    path('clinics/us/california/western-fertility-institute', views.wfi, name='wfi'),
    path('clinics/us/california/california-ivf-fertility-center', views.cifc, name='cifc'),
    path('clinics/us/california/northern-california-fertility-medical-center-roseville', views.ncfmcr, name='ncfmcr'),
    path('clinics/us/california/northern-california-fertility-medical-center-sacramento', views.ncfmcs, name='ncfmcs'),
    path('clinics/us/california/la-ivf-west-los-angeles', views.liwla, name='liwla'),
    path('clinics/us/california/la-ivf-pasadena', views.lip, name='lip'),
    path('clinics/us/california/la-ivf-chino-hills', views.lich, name='lich'),
    path('clinics/us/alabama/center-for-reproductive-medicine', views.tcfrm, name='tcfrm'),
    path('clinics/us/alabama/alabama-fertility', views.af, name='af'),
    path('clinics/us/arizona/troche-fertility-glendale', views.tfg, name='tfg'),
    path('clinics/us/arizona/troche-fertility-mesa', views.tfm, name='tfm'),
    path('clinics/us/arizona/troche-fertility-scottsdale', views.tfc, name='tfc'),
    path('clinics/us/arizona/southwest-fertility-center', views.sfc, name='sfc'),
    path('clinics/us/arizona/advanced-fertility-care-scottsdale', views.afcs, name='afcs'),
    path('clinics/us/arizona/advanced-fertility-care-mesa', views.afcm, name='afcm'),
    path('clinics/us/arizona/arizona-associates-for-reproductive-health-scottsdale', views.aafrhs, name='aafrhs'),
    path('clinics/us/arizona/arizona-associates-for-reproductive-health-gilbert', views.aafrhg, name='aafrhg'),
    path('clinics/us/arizona/bloom-reproductive-institute-scottsdale', views.bris, name='bris'),
    path('clinics/us/arizona/bloom-reproductive-institute-gilbert', views.brig, name='brig'),
    path('clinics/us/arizona/boston-ivf-arizona-center-scottsdale', views.biacs, name='biacs'),
    path('clinics/us/arizona/boston-ivf-arizona-center-chandler', views.biacch, name='biacch'),
    path('clinics/us/arizona/boston-ivf-arizona-center-peoria', views.biacp, name='biacp'),
    path('clinics/us/arizona/boston-ivf-arizona-center-flagstaff', views.biacf, name='biacf'),
    path('clinics/us/arizona/ivf-phoenix', views.ip, name='ip'),
    path('clinics/us/arizona/fertility-treatment-center', views.ftc, name='ftc'),
    path('clinics/us/arizona/arizona-reproductive-institute-fertility-clinic', views.arifc, name='arifc'),
    path('clinics/us/new-jersey/irms-clark-office', views.irmsco, name='irmsco'),
    path('clinics/us/new-jersey/irms-east-windsor-office', views.irmsewo, name='irmsewo'),
    path('clinics/us/new-jersey/irms-hackensack-office', views.irmsho, name='irmsho'),
    path('clinics/us/new-jersey/irms-hoboken-office', views.irmshbo, name='irmshbo'),
    path('clinics/us/new-jersey/irms-jersey-city-office', views.irmsnjo, name='irmsnjo'),
    path('clinics/us/new-jersey/irms-livingston-office', views.irmslo, name='irmslo'),
    path('clinics/us/new-jersey/irms-old-bridge-office', views.irmsobo, name='irmsobo'),
    path('clinics/us/new-york/chelsea-fertility-nyc', views.cfnyc, name='cfnyc'),
    path('clinics/us/new-york/ccrm-new-york-fertility-clinic', views.ccrmnyfc, name='ccrmnyfc'),
    path('clinics/us/arkansas/arkansas-fertility-gynecology', views.afg, name='afg'),
    path('clinics/us/colorado/ccrm-colorado-main-center-lone-tree', views.ccrmcmclt, name='ccrmcmclt'),
    path('clinics/us/colorado/ccrm-colorado-denver-office', views.ccrmcdo, name='ccrmcdo'),
    path('clinics/us/colorado/ccrm-colorado-louisville-office', views.ccrmclo, name='ccrmclo'),
    path('clinics/us/colorado/uc-advanced-reproductive-medicine-denver', views.ucarmd, name='ucarmd'),
    path('clinics/us/colorado/uc-advanced-reproductive-medicine-co-springs', views.ucarmcos, name='ucarmcos'),
    path('clinics/us/colorado/rocky-mountain-center-reproductive-medicine', views.rmcrm, name='rmcrm'),
    path('clinics/us/connecticut/cars-farmington', views.carsf, name='carsf'),
    path('clinics/us/connecticut/cars-hartford', views.carsh, name='carsh'),
    path('clinics/us/connecticut/cars-new-london', views.carsnl, name='carsnl'),
    path('clinics/us/connecticut/cars-branford', views.carsb, name='carsb'),
    path('clinics/us/connecticut/greenwich-fertility-greenwich', views.gfg, name='gfg'),
    path('clinics/us/connecticut/greenwich-fertility-stamford', views.gfs, name='gfs'),
    path('clinics/us/connecticut/rmact-norwalk', views.rmactn, name='rmactn'),
    path('clinics/us/connecticut/rmact-stamford', views.rmacts, name='rmacts'),
    path('clinics/us/connecticut/rmact-danbury', views.rmactd, name='rmactd'),
    path('clinics/us/connecticut/rmact-trumbull', views.rmactt, name='rmactt'),
    path('clinics/us/connecticut/park-avenue-fertility-trumbull', views.paft, name='paft'),
    path('clinics/us/connecticut/park-avenue-fertility-fairfield', views.paff, name='paff'),
    path('clinics/us/connecticut/park-avenue-fertility-norwalk', views.pafn, name='pafn'),
    path('clinics/us/delaware/dirm-newark', views.dirmn, name='dirmn'),
    path('clinics/us/delaware/dirm-milford', views.dirmm, name='dirmm'),
    path('clinics/us/delaware/radfertility-newark', views.radfn, name='radfn'),
    path('clinics/us/delaware/radfertility-wilmington', views.radfw, name='radfw'),
    path('clinics/us/delaware/radfertility-dover', views.radfd, name='radfd'),

    path('clinics/us/florida/boca-fertility', views.bocaf, name='bocaf'),
    path('clinics/us/florida/pbfc-boca-raton', views.pbfcbr, name='pbfcbr'),
    path('clinics/us/florida/pbfc-palm-beach-gardens', views.pbfcpbg, name='pbfcpbg'),
    path('clinics/us/florida/ffi-clearwater-office', views.ffico, name='ffico'),
    path('clinics/us/florida/ffi-tampa-office', views.ffito, name='ffito'),
    path('clinics/us/florida/conceptions-florida-coral-gables', views.cfcg, name='cfcg'),
    path('clinics/us/florida/conceptions-florida-miramar', views.cfm, name='cfm'),
    path('clinics/us/florida/jcrm-jacksonville', views.jcrmj, name='jcrmj'),
    path('clinics/us/florida/jcrm-gainesville', views.jcrmg, name='jcrmg'),
    path('clinics/us/florida/jcrm-panama-city', views.jcrmpc, name='jcrmpc'),
    path('clinics/us/florida/jcrm-orlando', views.jcrmo, name='jcrmo'),
    path('clinics/us/florida/rma-network-lake-mary', views.rmanlm, name='rmanlm'),
    path('clinics/us/florida/ivf-florida-wellington-fertility-center', views.ivffwfc, name='ivffwfc'),
    path('clinics/us/florida/ivf-florida-coral-gables-fertility-center', views.ivffcgfc, name='ivffcgfc'),
    path('clinics/us/florida/ivf-florida-pembroke-pines-fertility-center', views.ivfppfc, name='ivfppfc'),
    path('clinics/us/florida/ivf-florida-margate-fertility-center', views.ivffmfc, name='ivffmfc'),
    path('clinics/us/florida/ivf-florida-boca-raton-fertility-center', views.ivfbrfc, name='ivfbrfc'),
    path('clinics/us/florida/ivf-florida-jupiter-palm-beach-gardens-fertility-center', views.ivffjpbgfc, name='ivffjpbgfc'),
    path('clinics/us/florida/ivf-florida-port-lucie-fertility-clinic', views.ivffplfc, name='ivffplfc'),
    path('clinics/us/florida/viera-fertility-center', views.vfc, name='vfc'),
    path('clinics/us/florida/fivfcm-miami', views.fivfcm, name='fivfcm'),
    path('clinics/us/florida/fivfcm-miami-beach', views.fivfcmb, name='fivfcmb'),
    path('clinics/us/florida/fertility-genetics', views.fg, name='fg'),
    path('clinics/us/florida/ivfmd-miami', views.ivfmdm, name='ivfmdm'),
    path('clinics/us/florida/ivfmd-cooper-city', views.ivfmdcc, name='ivfmdcc'),
    path('clinics/us/florida/ivfmd-boca-raton', views.ivfmdbr, name='ivfmdbr'),
    path('clinics/us/florida/ivfmd-jupiter', views.ivfmdj, name='ivfmdj'),
    path('clinics/us/florida/ivfmd-naples', views.ivfmdn, name='ivfmdn'),
    path('clinics/us/florida/ivfmd-viera', views.ivfmdv, name='ivfmdv'),
    path('clinics/us/florida/sgf-tampa-westshore', views.sgftw, name='sgftw'),
    path('clinics/us/florida/sgf-brandon', views.sgfb, name='sgfb'),
    path('clinics/us/florida/sgf-wesley-chapel', views.sgfwc, name='sgfwc'),
    path('clinics/us/florida/rmg-north-tampa-office', views.rmgnto, name='rmgnto'),
    path('clinics/us/florida/rmg-south-tampa-office', views.rmgsto, name='rmgsto'),
    path('clinics/us/florida/rmg-clearwater-office', views.rmgco, name='rmgco'),
    path('clinics/us/florida/rmg-brandon-office', views.rmgbo, name='rmgbo'),
    path('clinics/us/florida/florida-institute-for-reproductive-sciences-technologies', views.fifrst, name='fifrst'),
    path('clinics/us/florida/advanced-reproductive-specialists-winter-park', views.arswp, name='arswp'),
    path('clinics/us/florida/ivf-orlando-winter-park', views.ivfowp, name='ivfowp'),
    path('clinics/us/florida/fertility-center-assisted-reproduction-endocrinology', views.fcare, name='fcare'),
    #GEORGIA
    path('clinics/us/georgia/aspire-fertility-atlanta', views.afa, name='afa'),
    path('clinics/us/georgia/acrm-atlanta-perimetr', views.acrmap, name='acrmap'),
    path('clinics/us/georgia/acrm-atlanta-buckhead', views.acrmab, name='acrmab'),
    path('clinics/us/georgia/acrm-johns-creek', views.acrmjc, name='acrmjc'),
    path('clinics/us/georgia/acrm-marietta', views.acrmm, name='acrmm'),
    path('clinics/us/georgia/massey-fertility-services', views.mfs, name='mfs'),
    path('clinics/us/georgia/servy-fertility-institute', views.sfi, name='sfi'),
    path('clinics/us/georgia/sgf-atlanta-northside', views.sgfan, name='sgfan'),
    path('clinics/us/georgia/sgf-alpharetta', views.sgfa, name='sgfa'),
    path('clinics/us/georgia/sgf-buckhead-piedmont', views.sgfbp, name='sgfbp'),
    path('clinics/us/georgia/sgf-marietta', views.sgfm, name='sgfm'),
    path('clinics/us/georgia/reproductive-biology-associates–main-office', views.rbamo, name='rbamo'),
    path('clinics/us/georgia/reproductive-biology-associates–marietta', views.rbam, name='rbam'),
    path('clinics/us/georgia/reproductive-biology-associates–fayetteville', views.rbaf, name='rbaf'),
    path('clinics/us/georgia/reproductive-biology-associates–lawrenceville', views.rbal, name='rbal'),
    path('clinics/us/georgia/reproductive-biology-associates–cumming', views.rbac, name='rbac'),
    path('clinics/us/georgia/reproductive-biology-associates–piedmont-hospital', views.rbaph, name='rbaph'),
    path('clinics/us/georgia/reproductive-biology-associates–cartersville', views.rbacar, name='rbacar'),
    #HAWAII
    path('clinics/us/hawaii/advanced-reproductive-center-hawaii', views.arch, name='arch'),
    path('clinics/us/hawaii/armgh-honolulu', views.armghh, name='armghh'),
    path('clinics/us/hawaii/armgh-kailua', views.armghk, name='armghk'),
    path('clinics/us/hawaii/pacific-in-vitro-fertilization-institute', views.pivfi, name='pivfi'),
    #IOWA
    path('clinics/us/iowa/mid-iowa-fertility', views.mif, name='mif'),
    #IDAHO
    path('clinics/us/idaho/idaho-center-reproductive-medicine', views.icrm, name='icrm'),
    #ILLINOIS
    path('clinics/us/illinois/center-reproductive-care', views.crc, name='crc'),
    path('clinics/us/illinois/fci-buffalo-grove-clinic', views.fcibgc, name='fcibgc'),
    path('clinics/us/illinois/fci-chicago-north-clinic', views.fcicnc, name='fcicnc'),
    path('clinics/us/illinois/fci-glenview-clinic', views.fcigc, name='fcigc'),
    path('clinics/us/illinois/fci-highland-park-clinic', views.fcihpc, name='fcihpc'),
    path('clinics/us/illinois/fci-hinsdale-clinic', views.fcihc, name='fcihc'),
    path('clinics/us/illinois/fci-hoffman-estates-clinic', views.fcihec, name='fcihec'),
    path('clinics/us/illinois/fci-lindenhurst-clinic', views.fcilc, name='fcilc'),
    path('clinics/us/illinois/fci-tinley-park-clinic', views.fcitpc, name='fcitpc'),
    path('clinics/us/illinois/fci-warrenville-clinic', views.fciwc, name='fciwc'),
    path('clinics/us/illinois/ihr-chicago', views.ihrc, name='ihrc'),
    path('clinics/us/illinois/ihr-oakbrook', views.ihro, name='ihro'),
    path('clinics/us/illinois/vios-fertility-institute-chicago-aurora', views.vfica, name='vfica'),
    path('clinics/us/illinois/vios-fertility-institute-chicago-wicker-park', views.vficwp, name='vficwp'),
    path('clinics/us/illinois/vios-fertility-institute-chicago-west-loop-ivf-lab', views.vficwlil, name='vficwlil'),
    path('clinics/us/illinois/vios-fertility-institute-chicago-glenview', views.vficg, name='vficg'),
    path('clinics/us/illinois/vios-fertility-institute-chicago-hoffman-estates', views.vfiche, name='vfiche'),
    path('clinics/us/illinois/davies-fertility-ivf-specialists', views.dfis, name='dfis'),
    path('clinics/us/illinois/hinsdale-center-reproduction', views.hcr, name='hcr'),
    path('clinics/us/illinois/invia-fertility-specialists-arlington-heights', views.ifsah, name='ifsah'),
    path('clinics/us/illinois/invia-fertility-specialists-crystal-lake', views.ifscl, name='ifscl'),
    path('clinics/us/illinois/invia-fertility-specialists-hoffman-estates', views.ifshe, name='ifshe'),
    path('clinics/us/illinois/invia-fertility-specialists-northbrook', views.ifsn, name='ifsn'),
    path('clinics/us/illinois/ivf1', views.ivf1, name='ivf1'),
    path('clinics/us/illinois/rmi-bloomingdale', views.rmib, name='rmib'),
    path('clinics/us/illinois/rmi-chicago', views.rmic, name='rmic'),
    path('clinics/us/illinois/rmi-elmhurst', views.rmiel, name='rmiel'),
    path('clinics/us/illinois/rmi-evanston', views.rmiev, name='rmiev'),
    path('clinics/us/illinois/rmi-northbrook', views.rminb, name='rminb'),
    path('clinics/us/illinois/rmi-oak-brook', views.rmiob, name='rmiob'),
    path('clinics/us/illinois/rmi-oak-lawn', views.rmiol, name='rmiol'),
    path('clinics/us/illinois/chicago-ivf-orland-park–southwest', views.civfops, name='civfops'),
    path('clinics/us/illinois/chicago-ivf-stcharles–northwest', views.civfscn, name='civfscn'),
    path('clinics/us/illinois/chicago-ivf-naperville–west', views.civfnw, name='civfnw'),
    #INDIANA
    path('clinics/us/indiana/ihr-valparaiso', views.ihrval, name='ihrval'),
    path('clinics/us/indiana/midwest-fertility-carmel', views.mfcar, name='mfcar'),
    path('clinics/us/indiana/midwest-fertility-fort-wayne', views.mffortwayne, name='mffortwayne'),
    path('clinics/us/indiana/chicago-ivf-valparaiso', views.civfval, name='civfval'),
    path('clinics/us/indiana/chicago-ivf-munster', views.civfmun, name='civfmun'),
    path('clinics/us/indiana/partners-reproductive-health-munster', views.prhmun, name='prhmun'),
    path('clinics/us/indiana/family-beginnings', views.fbeg, name='fbeg'),
    path('clinics/us/indiana/indiana-fertility-institute', views.ifinst, name='ifinst'),
    path('clinics/us/indiana/reproductive-care-indiana-main-office', views.rcimo, name='rcimo'),
    path('clinics/us/indiana/reproductive-care-indiana-terre-haute', views.rcith, name='rcith'),
    path('clinics/us/indiana/reproductive-care-indiana-lafayette', views.rcilaf, name='rcilaf'),
    path('clinics/us/indiana/reproductive-care-indiana-bloomington-mc', views.rcibmc, name='rcibmc'),
    path('clinics/us/indiana/reproductive-care-indiana-bloomington-ws', views.rcibws, name='rcibws'),
    #KANSAS
    path('clinics/us/kansas/midwest-reproductive-center', views.midrepc, name='midrepc'),
    #KENTUCKY
    path('clinics/us/kentucky/fertility-endocrine-associates', views.ferendas, name='ferendas'),
    #LOUISIANA
    path('clinics/us/louisiana/fertility-answers-lafayette', views.feanla, name='feanla'),
    path('clinics/us/louisiana/fertility-answers-baton-rouge', views.feanbaro, name='feanbaro'),
    path('clinics/us/louisiana/fertility-answers-covington', views.feanco, name='feanco'),
    path('clinics/us/louisiana/fertility-answers-lake-charles', views.feanlach, name='feanlach'),
    path('clinics/us/louisiana/fi-mandeville', views.fiman, name='fiman'),
    path('clinics/us/louisiana/fi-metairie', views.fimet, name='fimet'),
    path('clinics/us/louisiana/fi-baton-rouge', views.fibaro, name='fibaro'),
    path('clinics/us/louisiana/audubon-fertility', views.audfer, name='audfer'),
    path('clinics/us/louisiana/arklatex-fertility-reproductive-medicine', views.arkferrepmed, name='arkferrepmed'),
    #MAINE
    path('clinics/us/maine/fcne-bangor-center', views.fcnebc, name='fcnebc'),
    path('clinics/us/maine/boston-ivf-bangor-fertility-center', views.bivfbfc, name='bivfbfc'),
    path('clinics/us/maine/boston-ivf-portland-fertility-center', views.bivfpfc, name='bivfpfc'),
    #MARYLAND
    #MASSACHUSETTS
    path('clinics/us/massachusetts/massachusetts-general-hospital-fertility-center', views.masghfc, name='masghfc'),
    path('clinics/us/massachusetts/ccrm-boston-main-center', views.ccrmbmc, name='ccrmbmc'),
    path('clinics/us/massachusetts/ccrm-metrowest-office', views.ccrmmo, name='ccrmmo'),
    path('clinics/us/massachusetts/ccrm-south-shore-office', views.ccrmsso, name='ccrmsso'),
    path('clinics/us/massachusetts/boston-ivf-tufts-medical-fertility-center', views.bivfmfc, name='bivfmfc'),
    path('clinics/us/massachusetts/boston-ivf-downtown-boston-fertility-center', views.bivfdbfc, name='bivfdbfc'),
    path('clinics/us/massachusetts/boston-ivf-lexington-fertility-center', views.bivflfc, name='bivflfc'),
    path('clinics/us/massachusetts/boston-ivf-quincy-fertility-center', views.bivfqfc, name='bivfqfc'),
    path('clinics/us/massachusetts/boston-ivf-waltham-fertility-center', views.bivfwfc, name='bivfwfc'),
    path('clinics/us/massachusetts/boston-ivf-stoneham-fertility-center', views.bivfsfc, name='bivfsfc'),
    path('clinics/us/massachusetts/fertility-centers-new-england-leominster-center', views.fcnelc, name='fcnelc'),
    path('clinics/us/massachusetts/fertility-centers-new-england-reading-center', views.fcnerc, name='fcnerc'),
    path('clinics/us/massachusetts/fertility-centers-new-england-danvers-center', views.fcnedc, name='fcnedc'),
    path('clinics/us/massachusetts/fertility-centers-new-england-braintree-center', views.fcnebce, name='fcnebce'),
    path('clinics/us/massachusetts/fertility-centers-new-england-boston-center', views.fcnebcen, name='fcnebcen'),
    #MICHIGAN
    path('clinics/us/michigan/ivf-michigan-fertility-center-ann-arbor-fertility-center', views.ivfmfcaafc, name='ivfmfcaafc'),
    path('clinics/us/michigan/ivf-michigan-fertility-center-bloomfield-hills-fertility-center', views.ivfmfcbhfc, name='ivfmfcbhfc'),
    path('clinics/us/michigan/ivf-michigan-fertility-center-cheboygan-fertility-center', views.ivfmfcchebfc, name='ivfmfcchebfc'),
    path('clinics/us/michigan/ivf-michigan-fertility-center-dearborn-fertility-center', views.ivfmfcdfc, name='ivfmfcdfc'),
    path('clinics/us/michigan/ivf-michigan-fertility-center-east-lansing-fertility-center', views.ivfmfcelfc, name='ivfmfcelfc'),
    path('clinics/us/michigan/ivf-michigan-fertility-center-macomb-fertility-center', views.ivfmfcmfc, name='ivfmfcmfc'),
    path('clinics/us/michigan/ivf-michigan-fertility-center-petoskey-fertility-center', views.ivfmfcpfc, name='ivfmfcpfc'),
    path('clinics/us/michigan/ivf-michigan-fertility-center-saginaw-fertility-center', views.ivfmfcsfc, name='ivfmfcsfc'),
    path('clinics/us/michigan/ivf-michigan-fertility-center-toledo-fertility-center', views.ivfmfctfc, name='ivfmfctfc'),
    path('clinics/us/michigan/gago-center-for-fertility-brighton', views.gcffb, name='gcffb'),
    path('clinics/us/michigan/gago-center-for-fertility-lansing', views.ggcffl, name='ggcffl'),
    path('clinics/us/michigan/gago-center-for-fertility-ann-arbor', views.ggcffaa, name='ggcffaa'),
    path('clinics/us/michigan/the-fertility-center-grand-rapids', views.tfcgr, name='tfcgr'),
    path('clinics/us/michigan/the-fertility-center-mason', views.tfcm, name='tfcm'),
    path('clinics/us/michigan/the-fertility-center-kalamazoo', views.tfck, name='tfck'),
    path('clinics/us/michigan/the-fertility-center-traverse-city', views.tfctc, name='tfctc'),
    path('clinics/us/michigan/ivf-michigan-rochester-hills', views.ivfmrh, name='ivfmrh'),
    path('clinics/us/michigan/ivf-michigan-flint', views.ivfmf, name='ivfmf'),
    path('clinics/us/michigan/ivf-michigan-dearborn', views.ivfmd, name='ivfmd'),
    path('clinics/us/michigan/reproductive-medicine-associates-of-michigan', views.rmaom, name='rmaom'),
    #MINNESOTA
    path('clinics/us/minnesota/ccrm-minneapolis', views.cccrmmin, name='cccrmmin'),
    path('clinics/us/minnesota/midwest-center-for-reproductive-health', views.midcfrh, name='midcfrh'),
    path('clinics/us/minnesota/center-for-reproductive-medicine-minneapolis', views.cenfrmmin, name='cenfrmmin'),
    path('clinics/us/minnesota/center-for-reproductive-medicine-st-paul', views.cenfrmstp, name='cenfrmstp'),
    path('clinics/us/minnesota/center-for-reproductive-medicine-western-ob-gyn', views.cenfrmwesog, name='cenfrmwesog'),
    path('clinics/us/minnesota/center-for-reproductive-medicine-st-lukes-obstetrics-gynecology-associates', views.cenfremstluobgyna, name='cenfremstluobgyna'),
    path('clinics/us/minnesota/reproductive-medicine-infertility-associates-woodbury', views.repmeinaswoo, name='repmeinaswoo'),
    path('clinics/us/minnesota/reproductive-medicine-infertility-associates-edina', views.repmeinasedi, name='repmeinasedi'),
]
