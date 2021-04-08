from django.contrib import sitemaps
from django.urls import reverse
from base import views
from searchLocationsRegionsUS import views
from location import views
from clinicsUS import views

class ClinicsViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return [
        'pragamedica',
        'fertilityportx',
        'praguefertilitycentre',
        'gynemfertilityclinic',
        'gennet',
        'medicaltravelczechrep',
        'pronatalplusprague',
        'pronatalsanatoriumprague',
        'ivfcube',
        'ivfzlinczechrep',
        'reprofitbrno',
        'reprogenesis',
        'pronatalkolin',
        'pronatalreproceskebudejovice',
        'pronatalnordteplice',
        'pronatalspakarlovyvary',
        'reprofitostrava',
        'medistella',

        #Spain
        'ivfspainalicante',
        'ivialicante',
        'clinicadefertilidadbarcelonaivf',
        'fertilabbarcelona',
        'institutmarquesbarcelona',
        'ivfforyou',
        'gravida',
        'ferttyinternational',
        'ivibarcelona',
        'fivmarbellabarcelona',
        'ivfspainmadrid',
        'fertilitymadrid',
        'evafertilityclinicmadrid',
        'ivimadridaravaca',
        'clinicatambre',
        'fertilityclinichru',
        'fivmarbellamadrid',
        'ivimalaga',
        'fivmarbellamalaga',
        'hcfertility',
        'clinicafertia',
        'ivisevilla',
        'inebir',
        'ginemedsevilla',
        'ivivalencia',
        'equipojuanacrespo',
        'unidaddereproduccionasistidaimedvalencia',
        'creavalencia',
        'imerinstitutodemedicinareproductiva',

        #United Kingdom
        'aberfercen',
        'carefertbath',
        'belffert',
        'carefertbirmingh',
        'createfertbirmin',
        'bmitheprioryhosp',
        'careferttamworth',
        'stjudesfertclinic',
        'completefertcentbourn',
        'poundburyfertdorset',
        'brightfertasso',
        'agoragynandfertcentre',
        'abcivfbristol',
        'bristolcentreforrepromedicine',
        'crgwbristol',
        'createfertbristol',
        'bristolcenforrepromedspireclinic',
        'londonwomensclinicbristol',
        'bournhallcliniccambridge',
        'cambridgeivf',
        'crgwcardiff',
        'londonwomenscliniccardiff',
        'walesfertilityinstitutecardiff',
        'bournhallcliniccolchester',
        'nurturefertburtsatclinic',
        'fertilityexeter',
        'gcrmfertilityglasgow',
        'semovoglasgow',
        'hullivfunit',
        'simplyfertilitychelm',
        'bournhallclinicwockford',
        'leedsfertilityclinic',
        'semovoleeds',
        'xyfertility',
        'carefertilitychester',
        'carefertilityliverpool',
        'thehewittfertilitycentreliverpool',
        'semovoliverpool',
        'centreforreproductivehealth',
        'londonwomensclinicbrentwood',
        'londonwomensclinicharrow',
        'abcivfharleystreet',
        'abcivfwimbledon',
        'assistedreproandgynaecologycentre',
        'cityfertility',
        'createfertistpauls',
        'fertilityplusfertilityclinic',
        'londonwomensclinicharleystreet',
        'poundburyfertilitylondon',
        'semovolondon',
        'londonwomenscliniclondonbridge',
        'thamesvalleyfertility',
        'ivflondonelstree',
        'hertsandessexfertilitycentre',
        'bostonplace',
        'carefertilitylondon',
        'conceptfertility',
        'createfertilitywimbledon',
        'evewell',
        'thefertilitygynaecologyacademy',
        'harleystreetfertilityclinic',
        'homertonfertilitycentre',
        'ivilondon',
        'kingsfertility',
        'listerfertilityclinic',
        'createfertilityhertfordshire',
        'manchesterfertility',
        'semovomanchestersouth',
        'thehewittfertilitycentreknutsford',
        'aurorareprohealthaltrincham',
        'abcivfmanchester',
        'createfertilitymanchester',
        'semovomanchestercitycentre',
        'fertilityfusion',
        'carefertilitymanchester',
        'londonwomensclinicdarlington',
        'newcastlefertilitycentre',
        'bournhallclinicnorwich',
        'nurturefertilitynottingham',
        'carefertilitynottingham',
        'createfertilityoxford',
        'oxfordfertility',
        'abcivfoxford',
        'bournhallclinicpeterborough',
        'crgwplymouth',
        'completefertilitycentreportsmouth',
        'salisburyfertcentre',
        'nurturefertilitychesterfield',
        'carefertilitysheffield',
        'completefertilitycentresouthampton',
        'wessexfertility',
        'walesfertilityinstituteneath',
        'crgwswansea',
        'londonwomensclinicswansea',

        #United States
        'wfi',
        'cifc',
        'ncfmcr',
        'ncfmcs',
        'liwla',
        'lip',
        'lich',
        'tcfrm',
        'af',
        'aminstrepbir',
        'aminstrephomeb',
        'newlifemobile',
        'newlifedothan',
        'fertinstofnorthal',
        'huntsrepromed',
        'artfertproofal',
        'tfg',
        'tfm',
        'tfc',
        'sfc',
        'afcs',
        'afcm',
        'aafrhs',
        'aafrhg',
        'bris',
        'brig',
        'biacs',
        'biacch',
        'biacp',
        'biacf',
        'ip',
        'ftc',
        'arifc',
        'afg',
        'ccrmcmclt',
        'ccrmcdo',
        'ccrmclo',
        'ucarmd',
        'ucarmcos',
        'rmcrm',
        'carsf',
        'carsh',
        'carsnl',
        'carsb',
        'gfg',
        'gfs',
        'rmactn',
        'rmacts',
        'rmactd',
        'rmactt',
        'paft',
        'paff',
        'pafn',
        'dirmn',
        'dirmm',
        'radfn',
        'radfw',
        'radfd',
        'bocaf',
        'pbfcbr',
        'pbfcpbg',
        'ffico',
        'ffito',
        'cfcg',
        'cfm',
        'jcrmj',
        'jcrmg',
        'jcrmpc',
        'jcrmo',
        'rmanlm',
        'ivffwfc',
        'ivffcgfc',
        'ivfppfc',
        'ivffmfc',
        'ivfbrfc',
        'ivffjpbgfc',
        'ivffplfc',
        'vfc',
        'fivfcm',
        'fivfcmb',
        'fg',
        'ivfmdm',
        'ivfmdcc',
        'ivfmdbr',
        'ivfmdj',
        'ivfmdn',
        'ivfmdv',
        'sgftw',
        'sgfb',
        'sgfwc',
        'rmgnto',
        'rmgsto',
        'rmgco',
        'rmgbo',
        'fifrst',
        'arswp',
        'ivfowp',
        'fcare',
        'afa',
        'acrmap',
        'acrmab',
        'acrmjc',
        'acrmm',
        'mfs',
        'sfi',
        'sgfan',
        'sgfa',
        'sgfbp',
        'sgfm',
        'rbamo',
        'rbam',
        'rbaf',
        'rbal',
        'rbac',
        'rbaph',
        'rbacar',
        'cnyferticentatlanta',
        'coastalfertispecsavannah',
        'arch',
        'armghh',
        'armghk',
        'pivfi',
        'mif',
        'icrm',
        'reprocarecenteridahofalls',
        'crc',
        'fcibgc',
        'fcicnc',
        'fcigc',
        'fcihpc',
        'fcihc',
        'fcihec',
        'fcilc',
        'fcitpc',
        'fciwc',
        'ihrc',
        'ihro',
        'vfica',
        'vficwp',
        'vficwlil',
        'vficg',
        'vfiche',
        'dfis',
        'hcr',
        'ifsah',
        'ifscl',
        'ifshe',
        'ifsn',
        'ivf1',
        'rmib',
        'rmic',
        'rmiel',
        'rmiev',
        'rminb',
        'rmiob',
        'rmiol',
        'civfops',
        'civfscn',
        'civfnw',
        'ihrval',
        'mfcar',
        'mffortwayne',
        'civfval',
        'civfmun',
        'prhmun',
        'fbeg',
        'ifinst',
        'rcimo',
        'rcith',
        'rcilaf',
        'rcibmc',
        'rcibws',
        'midrepc',
        'ferendas',
        'ifrhealthflo',
        'ifrhealthlou',
        'feanla',
        'feanbaro',
        'feanco',
        'feanlach',
        'fiman',
        'fimet',
        'fibaro',
        'audfer',
        'arkferrepmed',
        'fcnebc',
        'bivfbfc',
        'bivfpfc',
        'masghfc',
        'ccrmbmc',
        'ccrmmo',
        'ccrmsso',
        'bivfmfc',
        'bivfdbfc',
        'bivflfc',
        'bivfqfc',
        'bivfwfc',
        'bivfsfc',
        'fcnelc',
        'fcnerc',
        'fcnedc',
        'fcnebce',
        'fcnebcen',
        'ivfmfcaafc',
        'ivfmfcbhfc',
        'ivfmfcchebfc',
        'ivfmfcdfc',
        'ivfmfcelfc',
        'ivfmfcmfc',
        'ivfmfcpfc',
        'ivfmfcsfc',
        'ivfmfctfc',
        'gcffb',
        'ggcffl',
        'ggcffaa',
        'tfcgr',
        'tfcm',
        'tfck',
        'tfctc',
        'ivfmrh',
        'ivfmf',
        'ivfmd',
        'rmaom',
        'cccrmmin',
        'midcfrh',
        'cenfrmmin',
        'cenfrmstp',
        'cenfrmwesog',
        'cenfremstluobgyna',
        'repmeinaswoo',
        'repmeinasedi',
        'cenfrmmfc',
        'missrepmed',
        'vfichisl',
        'vfichiofa',
        'infeceofstlo',
        'mcrmferstlo',
        'mcrmferspring',
        'missofer',
        'shiforrepmestlofecl',
        'hearceforrepme',
        'greevalferpartners',
        'theferceoflasvegas',
        'sherinsfrepmedlasvegfecl',
        'redrofercen',
        'irmsco',
        'irmsewo',
        'irmsho',
        'irmshbo',
        'irmsnjo',
        'irmslo',
        'irmsobo',
        'Cenfoarepmedicinefer',
        'rmanetbasrid',
        'rmaneteaton',
        'rmanetenglewood',
        'rmanetfreehold',
        'rmanetmarlton',
        'rmanetmorristown',
        'rmanetprinceston',
        'rmanetsomerset',
        'rmanetspringfield',
        'rmanetwestorang',
        'unirepproassohasbhei',
        'unirepproassohoboken',
        'unirepproassowayne',
        'princetonivf',
        'delawvallinsoffergenmarlton',
        'delawvallinsoffergenvineland',
        'delawvallinsoffergenprinceton',
        'southjefecemarlton',
        'southjefeceburlington',
        'southjefecesewell',
        'southjefecetownship',
        'diamondinsmilburn',
        'diamondinsdover',
        'diamondinsmtlaurel',
        'diamondinsmtmelrosepark',
        'fertilinstofnewjernewyork',
        'damienfertpartshrewsbury',
        'damienfertpartnewjerseycity',
        'damienfertpartnewark',
        'islandrepsernewjer',
        'ferticentofnewmexico',
        'diamondinsgoshen',
        'cfnyc',
        'ccrmnyfc',
        'sherinsforrepmednewyorkferclinic',
        'greenwfertuck',
        'rmactnorwalk',
        'extendfert',
        'geneferrepromedibaypark',
        'geneferrepromediparkslope',
        'geneferrepromediforesthills',
        'geneferrepromedistatenisland',
        'geneferrepromedilongisland',
        'buffinferivfas',
        'hudsvallfert',
        'bostonivfalbany',
        'bostonivfsyracusy',
        'longislivfmelville',
        'longislivfeastpatchogue',
        'longislivfgardencity',
        'longislivfwestislip',
        'longislivflakesuccess',
        'longislivfstonybrooks',
        'nyulangonerepspenewyorkmineola',
        'nyulangonerepspenewyorkbrooklyn',
        'kindboynewyorkmedical',
        'kofifertgroupstatenisland',
        'kofifertgroupupperwestside',
        'kofifertgrouplowermanhattan',
        'sgfmanhattan',
        'newaymedical',
        'repromedassocnewyorkeastside',
        'repromedassocnewyorkwestside',
        'repromedassocnewyorkdowntown',
        'repromedassocnewyorkbrooklyn',
        'repromedassocnewyorkwestchester',
        'repromedassocnewyorkmountsinai',
        'islandreproservicesstatenisland',
        'cnyfercensyracuse',
        'cnyfercenalbany',
        'cnyfercenrochester',
        'cnyfercenbuffalo',
        'northcarcenfrepmedic',
        'reproendoassoofcharlotte',
        'reproendoassoofcharlottelakenorman',
        'atlanticreprmedspec',
        'carolinaconcerale',
        'carolinaconcewilmington',
        'carolinaconcehampstead',
        'carolinaconcegreenville',
        'carolfertinstgreens',
        'carolfertinstwinstonsalem',
        'carolfertinstcharlotte',
        'piedmoreproendogroupashe',
        'midwecenforreprohealfargo',
        'midwecenforreprohealminot',
        'ivfmichiganohio',
        'northeasternohiofertcen',
        'reprogyninferakron',
        'reprogyninfercolumbus',
        'reprogyninfercleveland',
        'reprogyninferyoungstown',
        'reprogyninfercanton',
        'springcreekfertility',
        'instituteforhealthcincinnati',
        'instituteforhealthwestche',
        'ohioreproductivemedicine',
        'fertilitywellnessinstohio',
        'ouphysiciansrepromedicine',
        'tulsafertcenter',
        'ormfertilityclidownportland',
        'ormfertilitycliwestsideportland',
        'ormfertilityclisouthportland',
        'sincerarepromedabington',
        'sincerarepromedbethlehem',
        'sincerarepromedfortwashington',
        'sincerarepromedkingofprussia',
        'sincerarepromedlancaster',
        'sincerarepromedlanghorne',
        'sincerarepromedlansdale',
        'sincerarepromedwestchester',
        'rmanetwork',
        'familyfertilitycenterbethlehem',
        'familyfertilitycenterclarkssummit',
        'mainlinefertilityrepromedicinebrynmawr',
        'mainlinefertilityrepromedicinepaoli',
        'mainlinefertilityrepromedicinephiladelphia',
        'mainlinefertilityrepromedicinewestchester',
        'mainlinefertilityrepromedicinehavertown',
        'mainlinefertilityrepromedicinereading',
        'shadygrovefertilityphiladelphia',
        'shadygrovefertilitychesterbrook',
        'shadygrovefertilitymechanicsburg',
        'shadygrovefertilitylancaster',
        'shadygrovefertilitywarrington',
        'puertoricofertilitycenter',
        'piedmontreproendogroupgreenville',
        'piedmontreproendogroupspartanburg',
        'piedmontreproendogroupcolumbia',
        'coastalfertspecimountpleasant',
        'coastalfertspecinorthcharleston',
        'coastalfertspecilexington',
        'coastalfertspecimyrtlebeach',
        'tenrepromedchattaivffertclin',
        'myfertilitycenterchatt',
        'myfertilitycenterknoxville',
        'tennesseefertiinstitute',
        'fertiassoofmemphis',
        'nashvillefertnashville',
        'nashvillefertmurfreesboro',
        'nashvillefertfranklin',
        'centerforreprohealthnash',
        'sherinsforrepmedicinedallas',
        'ccrmdallasfortworth',
        'ccrmhoustonmaincenter',
        'ccrmhoustonmedicalcenter',
        'ccrmhoustonsugarland',
        'aspirefertaustinfertilitycenter',
        'aspirefertbeecavefertcenter',
        'aspirefertadison',
        'aspirefertclearlake',
        'aspirefertfanninfece',
        'aspirefertkatyfertce',
        'aspirefertmainstreet',
        'aspirefertsugarlandfertcen',
        'aspirefertwillowbrookfertcent',
        'aspirefertsanantoniofertcenter',
        'aspirefertsatellitecliniclocation',
        'ivfmdcenterarlington',
        'ivfmdcenterirving',
        'austinfertrepmedwestlake',
        'austinfertrepmedsouthlocation',
        'austinfertrepmedroundrock',
        'texasfertilitycentercentralaustin',
        'texasfertilitycenterroundrock',
        'texasfertilitycentersouthaustin',
        'texasfertilitycenternewbraunfels',
        'texasfertilitycentersanantonio',
        'texasfertilitycentercorpuschristi',
        'centerforassistedreprobedford',
        'centerforassistedreprofortworth',
        'dallasfortworthfertilityassociates',
        'dallasfortworthfertilityassociatessouthlake',
        'dallasfortworthfertilityassociatesmedicalcity',
        'fertilitycenterofdallas',
        'repromedfertilitycenterdallas',
        'repromedfertilitycentergrapevine',
        'repromedfertilitycentermckinney',
        'repromedfertilitycenterrockwall',
        'repromedfertilitycentertyler',
        'repromedfertilitycentermckinneysurgicalcenter',
        'sherfertilityclinicdallas',
        'texascenterforreproductivehealth',
        'fortworthfertility',
        'dallasivffriscofertilityclinic',
        'dallasivfdallasfertilityclinic',
        'dallasivfmckinleyfertilityclinic',
        'dallasivfplanofertilityclinic',
        'dallasivftylerfertilityclinic',
        'fertilityspecialistsoftexasfrisco',
        'fertilityspecialistsoftexasdallas',
        'fertilityspecialistsoftexasrockwall',
        'fertilityspecialistsoftexassouthlake',
        'advancedfertilitycenteroftexasmemorialcity',
        'advancedfertilitycenteroftexasspring',
        'advancedfertilitycenteroftexascollegestation',
        'centerofreproductivemedicinehouston',
        'centerofreproductivemedicinememorialcity',
        'centerofreproductivemedicineclearlake',
        'centerofreproductivemedicinebeaumont',
        'houstonfertilityinstitutehoustonoffice',
        'houstonfertilityinstitutemedicalcentermemorialhermann',
        'houstonfertilityinstitutemedicalcenterwomanshospital',
        'houstonfertilityinstitutemedicalcenterkatyoffice',
        'houstonfertilityinstitutemedicalcentersugarland',
        'houstonfertilityinstitutemedicalcenterclearlakeoffice',
        'houstonfertilityinstitutemedicalcentermemorialcityoffice',
        'houstonfertilityinstitutemedicalcenterwillowbrookoffice',
        'houstonfertilityinstitutemedicalcenterwoodlandsoffice',
        'houstonfertilityinstitutemedicalcenterbeaumontoffice',
        'houstonfertilityinstitutemedicalcentercypresstoffice',
        'houstonfertilityinstitutemedicalcenterkingwoodoffice',
        'houstonfertilityinstitutemedicalcenterpearlandoffice',
        'odessaivf',
        'ivfplano',
        'fertilityceofsanantsanantoffice',
        'fertilityceofsanantstoneoakoffice',
        'hartivffertilityclinicwoodlands',
        'hartivffertilityclinickingwood',
        'utahfertilitycenterogden',
        'conceptionsfertility',
        'reproductivecarecenterclearfield',
        'reproductivecarecentersandy',
        'reproductivecarecenterpleasantgrove',
        'northeasternreproductivemedicinecolchester',
        'columbiafertilityassociatesarlington',
        'ccrmmaincenter',
        'ccrmcolumbia',
        'washingtonfertilitycenterannandale',
        'washingtonfertilitycenterfredericksburg',
        'washingtonfertilitycenterreston',
        'dominionfertilityarlington',
        'dominionfertilityfairfax',
        'reproductivemedicineandsurgerycenterofvirginiacharlottesville',
        'reproductivemedicineandsurgerycenterofvirginialynchburg',
        'geneticsivfinstitute',
        'virginiacenterforreproductivemedicine',
        'thenewhopecenterforreproductivemedicine',
        'orgfertilityclinicbellevue',
        'dominionfertilitywashington',
        'bellevuefertilityclinic',
        'pomafertility',
        'pacificnwfertilityseattle',
        'pacificnwfertilitybellevue',
        'seattlereproductivemedicineseattle',
        'seattlereproductivemedicinebellevue',
        'seattlereproductivemedicinetacoma',
        'seattlereproductivemedicinekirkland',
        'seattlereproductivemedicineeverett',
        'seattlereproductivemedicinespokane',
        'soundfertilitycare',
        'thecenterforreproductivehealth',
        'viosfertilityinstitutechicagomilwaukee',
        'viosfertilityinstitutechicagolakecountry',
        'wisconsinfertilityinstitute',
        'columbiafertilityassociateswashingtondc',
        'gwmedicalfacultyassociates',
        'nyulangonefertilitycenter',

        #Greece
        'newlifeivfclinic',
        'embryoclinic',
        'embryolab',
        'serumivfcenter',
        'ivfathenscenter',
        'embryolandivfcenterathens',
        'embiomedicalcenter',
        'mitosisivfclinic',
        'eugoniaassistedreproductionunit',
        'mediterraneanfertilityinstitute',

        #India
        'kiraninfertilitycenterbengaluru',
        'mannatfertilitycentre',
        'hyderabadwomenfertilitycentregachibowli',
        'indiaivfclinicgurgaon',
        'indiaivfclinicgwalior',
        'indiaivfclinichaldwani',
        'oasisfertilityhyderabadbanjarahills',
        'oasisfertilityhyderabadsecunderabad',
        'oasisfertilityhyderabaddilsukhnagar',
        'oasisfertilityhyderabadgachibowli',
        'oasisfertilityhyderabmiyapur',
        'kiraninfertilitycenterhyderabad',
        'kiraninfertilitycenterkothapet',
        'hegdefertilitymalakpet',
        'oasisfertchennai',
        'kiraninfertilitycenterchennai',
        'indiaivfclinicjammu',
        'hegdehospitalmadhapur',
        'indiaivfclinicmeerut',
        'indiaivfclinicnewdelhi',
        'selectivfnewdelhi',
        'indiraivfcentredelhi',
        'indiaivfclinicnoida',
        'oasisfertilitypune',
        'oasisfertilityranchi',
        'indiaivfclinicranchi',
        'indiaivfclinicrohtak',
        'oasisfertilityvadodara',
        'oasisfertilityvijayawada',
        'oasisfertilityvisakhapatnam',
        'oasisfertilitywarangal',

        #Cyprus
        'cyprusivfcentre',
        'britishcyprusivfhospital',
        'eurocareivf',
        'dogusfertilityclinic',
        'pedieosivfcenter',
        'crownivfcyprus',
        'dunyaivfcyprusfertilityclinic',
        'kyreniaivfcenter',

        #Mexico
        'iregaacapulco',
        'fertilityclinicamericas',
        'advancedfertilitycenterfertilitycentercancun',
        'newlifemexico',
        'iregacancun',
        'embryogengertilitycenterguasave',
        'enlistalofertilidadmexicociudaddemexico',
        'citmermedicinareproductiva',
        'embryogenfertilitycenterculiacan',
        'embryogenfertilitycenterhermosillo',
        'embryogenfertilitycentermazatlan',
        'mexicofertilitycenter',
        'embryogenfertilitycenternogales',
        'ivfvallarta',
        'surrogacymexico',
        'iregapuebla',
        ]

    def location(self, item):
        return reverse(item)
