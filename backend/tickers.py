"""
Universe of SET (Stock Exchange of Thailand) listed companies to screen.
Symbols use the Yahoo Finance suffix convention (".BK") since we pull
fundamental data from Yahoo Finance's free, keyless endpoints via yfinance.

This list covers essentially the full SET + mai common-stock, REIT, and
property/infrastructure-fund universe (~900 tickers), scraped from a public
exchange listing and filtered to Thai-domiciled securities only (company
name contains "PCL", "REIT", "Fund", or "Trust") -- this excludes the many
Thai DR (Depositary Receipt) products that track foreign stocks like NVDA,
AAPL, TSLA etc., which are not real SET-listed operating companies.
"""

SET_TICKERS = [
    "DELTA.BK",  # Delta Electronics (Thailand) PCL
    "PTT.BK",  # PTT PCL
    "ADVANC.BK",  # Advanced Info Service PCL
    "GULF.BK",  # Gulf Development PCL
    "AOT.BK",  # Airports of Thailand PCL
    "KTB.BK",  # Krung Thai Bank PCL
    "KBANK.BK",  # Kasikornbank PCL
    "PTTEP.BK",  # PTT Exploration and Production PCL
    "SCB.BK",  # SCB X PCL
    "TRUE.BK",  # True Corporation PCL
    "CPALL.BK",  # CP ALL PCL
    "BBL.BK",  # Bangkok Bank PCL
    "BDMS.BK",  # Bangkok Dusit Medical Services PCL
    "SCC.BK",  # The Siam Cement PCL
    "CPN.BK",  # Central Pattana PCL
    "BAY.BK",  # Bank of Ayudhya PCL
    "TTB.BK",  # TMBThanachart Bank PCL
    "CPF.BK",  # Charoen Pokphand Foods PCL
    "PTTGC.BK",  # PTT Global Chemical PCL
    "THAI.BK",  # Thai Airways International PCL
    "CRC.BK",  # Central Retail Corporation PCL
    "CPAXT.BK",  # CP Axtra PCL
    "BH.BK",  # Bumrungrad Hospital PCL
    "TOP.BK",  # Thai Oil PCL
    "OR.BK",  # PTT Oil and Retail Business PCL
    "GPSC.BK",  # Global Power Synergy PCL
    "SCGP.BK",  # SCG Packaging PCL
    "MINT.BK",  # Minor International PCL
    "TLI.BK",  # Thai Life Insurance PCL
    "IVL.BK",  # Indorama Ventures PCL
    "BEM.BK",  # Bangkok Expressway and Metro PCL
    "TISCO.BK",  # TISCO Financial Group PCL
    "KTC.BK",  # Krungthai Card PCL
    "AWC.BK",  # Asset World Corp PCL
    "CCET.BK",  # Cal-Comp Electronics (Thailand) PCL
    "KKP.BK",  # Kiatnakin Phatra Bank PCL
    "TCAP.BK",  # Thanachart Capital PCL
    "HMPRO.BK",  # Home Product Center PCL
    "RATCH.BK",  # Ratch Group PCL
    "WHA.BK",  # WHA Corporation PCL
    "BCP.BK",  # Bangchak Corporation PCL
    "MTC.BK",  # Muangthai Capital PCL
    "EGCO.BK",  # Electricity Generating PCL
    "COM7.BK",  # Com7 PCL
    "TFMAMA.BK",  # Thai President Foods PCL
    "BJC.BK",  # Berli Jucker PCL
    "KCE.BK",  # KCE Electronics PCL
    "TFG.BK",  # Thaifoods Group PCL
    "MRDIYT.BK",  # MR. D.I.Y. Holding (Thailand) PCL
    "CBG.BK",  # Carabao Group PCL
    "CENTEL.BK",  # Central Plaza Hotel PCL
    "TIDLOR.BK",  # Tidlor Holdings PCL
    "OSP.BK",  # Osotspa PCL
    "ITC.BK",  # i-Tail Corporation PCL
    "SPRC.BK",  # Star Petroleum Refining PCL
    "IRPC.BK",  # IRPC PCL
    "CPNREIT.BK",  # CPN Retail Growth Leasehold REIT
    "TU.BK",  # Thai Union Group PCL
    "BGRIM.BK",  # B.Grimm Power PCL
    "SCCC.BK",  # Siam City Cement PCL
    "SPI.BK",  # Saha Pathana Inter-Holding PCL
    "LH.BK",  # Land and Houses PCL
    "GUNKUL.BK",  # Gunkul Engineering PCL
    "FTREIT.BK",  # Frasers Property Thailand Industrial Freehold & Leasehold REIT
    "TTW.BK",  # TTW PCL
    "BLA.BK",  # Bangkok Life Assurance PCL
    "GLOBAL.BK",  # Siam Global House PCL
    "BA.BK",  # Bangkok Airways PCL
    "BKIH.BK",  # BKI Holdings PCL
    "BTG.BK",  # Betagro PCL
    "SAWAD.BK",  # Srisawad Corporation PCL
    "WHART.BK",  # WHA Premium Growth Freehold And Leasehold Real Estate Investment Trust
    "MBK.BK",  # MBK PCL
    "AMATA.BK",  # Amata Corporation PCL
    "HANA.BK",  # Hana Microelectronics PCL
    "RCL.BK",  # Regional Container Lines PCL
    "BTS.BK",  # BTS Group Holdings PCL
    "MEGA.BK",  # Mega Lifesciences PCL
    "SPALI.BK",  # Supalai PCL
    "AXTRART.BK",  # Axtra Future City Freehold And Leasehold Real Estate Investment Trust
    "CK.BK",  # CH. Karnchang PCL
    "WHAUP.BK",  # WHA Utilities and Power PCL
    "STGT.BK",  # Sri Trang Gloves (Thailand) PCL
    "TOA.BK",  # TOA Paint (Thailand) PCL
    "CREDIT.BK",  # Thai Credit Bank PCL
    "STA.BK",  # Sri Trang Agro-Industry PCL
    "BCH.BK",  # Bangkok Chain Hospital PCL
    "SIRI.BK",  # Sansiri PCL
    "PLANB.BK",  # Plan B Media PCL
    "AP.BK",  # AP (Thailand) PCL
    "LHFG.BK",  # LH Financial Group PCL
    "STECON.BK",  # Stecon Group PCL
    "AEONTS.BK",  # AEON Thana Sinsap (Thailand) PCL
    "TASCO.BK",  # Tipco Asphalt PCL
    "TVO.BK",  # Thai Vegetable Oil PCL
    "PRM.BK",  # Prima Marine PCL
    "EA.BK",  # Energy Absolute PCL
    "PB.BK",  # President Bakery PCL
    "RAM.BK",  # Ramkhamhaeng Hospital PCL
    "BCPG.BK",  # BCPG PCL
    "VGI.BK",  # VGI PCL
    "BAM.BK",  # Bangkok Commercial Asset Management PCL
    "CKP.BK",  # CK Power PCL
    "IMPACT.BK",  # IMPACT Growth Real Estate Investment Trust
    "JTS.BK",  # Jasmine Technology Solution PCL
    "M.BK",  # MK Restaurant Group PCL
    "ICHI.BK",  # Ichitan Group PCL
    "AURA.BK",  # Aurora Design PCL
    "SPC.BK",  # Saha Pathanapibul PCL
    "VIBHA.BK",  # Vibhavadi Medical Center PCL
    "SJWD.BK",  # SCGJWD Logistics PCL
    "ERW.BK",  # The Erawan Group PCL
    "STANLY.BK",  # Thai Stanley Electric PCL
    "AYUD.BK",  # Allianz Ayudhya Capital PCL
    "CHG.BK",  # Chularat Hospital PCL
    "TPIPL.BK",  # TPI Polene PCL
    "EPG.BK",  # Eastern Polymer Group PCL
    "JMT.BK",  # JMT Network Services PCL
    "FPT.BK",  # Frasers Property (Thailand) PCL
    "SKR.BK",  # Sikarin PCL
    "SGP.BK",  # Siamgas and Petrochemicals PCL
    "JMART.BK",  # Jaymart Group Holdings PCL
    "QH.BK",  # Quality Houses PCL
    "FORTH.BK",  # Forth Corporation PCL
    "TPIPP.BK",  # TPI Polene Power PCL
    "BCT.BK",  # Birla Carbon (Thailand) PCL
    "PSL.BK",  # Precious Shipping PCL
    "SAUCE.BK",  # Thaitheparos PCL
    "LHHOTEL.BK",  # LH Hotel Leasehold Real Estate Investment Trust
    "DMT.BK",  # Don Muang Tollway PCL
    "PR9.BK",  # Praram 9 Hospital PCL
    "UVAN.BK",  # Univanich Palm Oil PCL
    "THANI.BK",  # Ratchthani Leasing PCL
    "PSGC.BK",  # PSG Corporation PCL
    "THG.BK",  # Thonburi Healthcare Group PCL
    "TIPH.BK",  # Dhipaya Group Holdings PCL
    "AAV.BK",  # Asia Aviation PCL
    "PTL.BK",  # Polyplex (Thailand) PCL
    "DCC.BK",  # Dynasty Ceramic PCL
    "DOHOME.BK",  # Dohome PCL
    "MOSHI.BK",  # Moshi Moshi Retail Corporation PCL
    "CIMBT.BK",  # CIMB Thai Bank PCL
    "ACE.BK",  # Absolute Clean Energy PCL
    "SKY.BK",  # Sky ICT PCL
    "ROJNA.BK",  # Rojana Industrial Park PCL
    "PTG.BK",  # PTG Energy PCL
    "LHSC.BK",  # LH Shopping Centers Leasehold Real Estate Investment Trust
    "GFPT.BK",  # GFPT PCL
    "ICC.BK",  # I.C.C. International PCL
    "THCOM.BK",  # Thaicom PCL
    "BAREIT.BK",  # BA Airport Leasehold Real Estate Investment Trust
    "PSP.BK",  # P.S.P. Specialties PCL
    "SCAP.BK",  # Srisawad Capital 1969 PCL
    "STPI.BK",  # STP&I PCL
    "ALUCON.BK",  # Alucon PCL
    "MTI.BK",  # Muang Thai Insurance PCL
    "SAPPE.BK",  # Sappe PCL
    "RBF.BK",  # R&B Food Supply PCL
    "TTA.BK",  # Thoresen Thai Agencies PCL
    "DUSIT.BK",  # Dusit Thani PCL
    "KGI.BK",  # KGI Securities (Thailand) PCL
    "MGC.BK",  # Millennium Group Corporation (Asia) PCL
    "DITTO.BK",  # Ditto (Thailand) PCL
    "AIMIRT.BK",  # AIM Industrial Growth Freehold and Leasehold Real Estate Investment Tr
    "BLAND.BK",  # Bangkok Land PCL
    "SPCG.BK",  # SPCG PCL
    "EASTW.BK",  # Eastern Water Resources Development and Management PCL
    "SGC.BK",  # SG Capital PCL
    "TQM.BK",  # TQM Alpha PCL
    "SINGER.BK",  # Singer Thailand PCL
    "MC.BK",  # MC Group PCL
    "SCGD.BK",  # SCG Decor PCL
    "XO.BK",  # Exotic Food PCL
    "TGH.BK",  # Thai Group Holdings PCL
    "WHAIR.BK",  # WHA Industrial Leasehold Real Estate Investment Trust
    "TSTH.BK",  # Tata Steel (Thailand) PCL
    "SC.BK",  # SC Asset Corporation PCL
    "SISB.BK",  # SISB PCL
    "KAMART.BK",  # Karmarts PCL
    "AAI.BK",  # Asian Alliance International PCL
    "PSH.BK",  # Pruksa Holding PCL
    "JAS.BK",  # Jasmine International PCL
    "COCOCO.BK",  # Thai Coconut PCL
    "PRG.BK",  # PRG Corporation PCL
    "BBGI.BK",  # BBGI PCL
    "SA.BK",  # Siamese Asset PCL
    "NER.BK",  # North East Rubber PCL
    "SIS.BK",  # SiS Distribution (Thailand) PCL
    "SUC.BK",  # Saha-Union PCL
    "LANNA.BK",  # Lanna Resources PCL
    "SYNEX.BK",  # Synnex (Thailand) PCL
    "KSL.BK",  # Khon Kaen Sugar Industry PCL
    "ASK.BK",  # Asia Sermkij Leasing PCL
    "AIT.BK",  # Advanced Information Technology PCL
    "ASTR.BK",  # Astra Enterprise PCL
    "SAV.BK",  # Samart Aviation Solutions PCL
    "NEO.BK",  # Neo Corporate PCL
    "TITLE.BK",  # Rhom Bho Property PCL
    "ASW.BK",  # Assetwise PCL
    "ONEE.BK",  # The ONE Enterprise PCL
    "KTIS.BK",  # Kaset Thai International Sugar Corporation PCL
    "ILM.BK",  # Index Living Mall PCL
    "SAT.BK",  # Somboon Advance Technology PCL
    "BAFS.BK",  # Bangkok Aviation Fuel Services PCL
    "AIRA.BK",  # AIRA Capital PCL
    "MEDEZE.BK",  # Medeze Group PCL
    "SAK.BK",  # Saksiam Leasing PCL
    "GVREIT.BK",  # Golden Ventures Leasehold Real Estate Investment Trust
    "NSL.BK",  # NSL Foods PCL
    "PROSPECT.BK",  # Prospect Logistics and Industrial Freehold and Leasehold Real Estate I
    "PRINC.BK",  # Principal Capital PCL
    "CPTREIT.BK",  # C.P. Tower Leasehold Real Estate Investment Trust
    "PCE.BK",  # Petchsrivichai Enterprise PCL
    "TFM.BK",  # Thai Union Feedmill PCL
    "PM.BK",  # Premier Marketing PCL
    "KLINIQ.BK",  # The Klinique Medical Clinic PCL
    "HTC.BK",  # Haad Thip PCL
    "SNNP.BK",  # Srinanaporn Marketing PCL
    "ANI.BK",  # Asia Network International PCL
    "SSP.BK",  # Sermsang Power Corporation PCL
    "METCO.BK",  # Muramoto Electron (Thailand) PCL
    "ASIAN.BK",  # Asian Sea Corporation PCL
    "TKN.BK",  # Taokaenoi Food & Marketing PCL
    "UTP.BK",  # United Paper PCL
    "KCG.BK",  # KCG Corporation PCL
    "TURTLE.BK",  # Super Turtle PCL
    "NEX.BK",  # Nex Point PCL
    "SRICHA.BK",  # Sriracha Construction PCL
    "SHR.BK",  # S Hotels and Resorts PCL
    "STELLA.BK",  # Stella X PCL
    "KYE.BK",  # Kang Yong Electric PCL
    "TNL.BK",  # Thanulux PCL
    "LRH.BK",  # Laguna Resorts & Hotels PCL
    "VIH.BK",  # Srivichaivejvivat PCL
    "FSMART.BK",  # Forth Smart Service PCL
    "SABINA.BK",  # Sabina PCL
    "SHANG.BK",  # Shangri-La Hotel PCL
    "SAMART.BK",  # Samart Corporation PCL
    "SMPC.BK",  # Sahamitr Pressure Container PCL
    "ROCTEC.BK",  # Roctec Global PCL
    "POPF.BK",  # Prime Office Leasehold Property Fund
    "AH.BK",  # AAPICO Hitech PCL
    "TR.BK",  # Thai Rayon PCL
    "PIN.BK",  # Pinthong Industrial Park PCL
    "XPG.BK",  # XSpring Capital PCL
    "TNH.BK",  # Thai Nakarin Hospital PCL
    "MAJOR.BK",  # Major Cineplex Group PCL
    "CMR.BK",  # Chiang Mai Ram Medical Business PCL
    "NYT.BK",  # Namyong Terminal PCL
    "NCAP.BK",  # Next Capital PCL
    "GGC.BK",  # Global Green Chemicals PCL
    "FUTURERT.BK",  # Future City Leasehold Real Estate Investment Trust
    "ORI.BK",  # Origin Property PCL
    "GLAND.BK",  # Grand Canal Land PCL
    "S_J.BK",  # S & J International Enterprises PCL
    "ASP.BK",  # Asia Plus Group Holdings PCL
    "BGC.BK",  # BG Container Glass PCL
    "MST.BK",  # Maybank Securities (Thailand) PCL
    "RJH.BK",  # Rajthanee Hospital PCL
    "SNP.BK",  # S&P Syndicate PCL
    "ADVICE.BK",  # Advice IT Infinite PCL
    "ALLY.BK",  # Ally Freehold And Leasehold Real Estate Investment Trust
    "DRT.BK",  # Diamond Building Products PCL
    "PCSGH.BK",  # P.C.S. Machine Group Holding PCL
    "TURBO.BK",  # Ngernturbo PCL
    "TPRIME.BK",  # Thailand Prime Property Freehold and Leasehold Real Estate Investment 
    "BOL.BK",  # Business Online PCL
    "TMAN.BK",  # T.Man Pharmaceutical PCL
    "SMT.BK",  # Stars Microelectronics (Thailand) PCL
    "FM.BK",  # Food Moments PCL
    "BBIK.BK",  # Bluebik Group PCL
    "BEC.BK",  # BEC World PCL
    "WPH.BK",  # Wattanapat Hospital Trang PCL
    "LALIN.BK",  # Lalin Property PCL
    "EKH.BK",  # Ekachai Medical Care PCL
    "TMD.BK",  # Thai Metal Drum Manufacturing PCL
    "TSC.BK",  # Thai Steel Cable PCL
    "OHTL.BK",  # OHTL PCL
    "SPA.BK",  # Siam Wellness Group PCL
    "TACC.BK",  # T.A.C. Consumer PCL
    "SPG.BK",  # Siam Pan Group PCL
    "MCOT.BK",  # MCOT PCL
    "BOFFICE.BK",  # Bhiraj Office Leasehold Real Estate Investment Trust
    "SKN.BK",  # S.Kijchai Enterprise PCL
    "TKS.BK",  # T.K.S. Technologies PCL
    "TRT.BK",  # Tirathai PCL
    "TSTE.BK",  # TSTE PCL
    "LST.BK",  # Lam Soon (Thailand) PCL
    "TEAM.BK",  # Team Precision PCL
    "NNCL.BK",  # Nava Nakorn PCL
    "MCS.BK",  # M.C.S. Steel PCL
    "PLAT.BK",  # The Platinum Group PCL
    "TMT.BK",  # TMT Steel PCL
    "KBS.BK",  # Khonburi Sugar PCL
    "MEB.BK",  # MEB Corporation PCL
    "DREIT.BK",  # Dusit Thani Freehold and Leasehold Real Estate Investment Trust
    "TKC.BK",  # Turnkey Communication Services PCL
    "PCC.BK",  # Precise Corporation PCL
    "BIZ.BK",  # Business Alignment PCL
    "TVH.BK",  # Thaivivat Holdings PCL
    "III.BK",  # Triple i Logistics PCL
    "INSET.BK",  # Infraset PCL
    "HUMAN.BK",  # Humanica PCL
    "AU.BK",  # After You PCL
    "HENG.BK",  # Heng Leasing and Capital PCL
    "LOXLEY.BK",  # Loxley PCL
    "S.BK",  # Singha Estate PCL
    "KGEN.BK",  # King Gen PCL
    "SMO.BK",  # Smothong Group PCL
    "VNG.BK",  # Vanachai Group PCL
    "PT.BK",  # Premier Technology PCL
    "TOG.BK",  # Thai Optical Group PCL
    "TPAC.BK",  # Thai Plaspac PCL
    "TEGH.BK",  # Thai Eastern Group Holdings PCL
    "SUPER.BK",  # Super Energy Corporation PCL
    "TIPCO.BK",  # Tipco Foods PCL
    "INOX.BK",  # POSCO-Thainox PCL
    "SCG.BK",  # Ratch Pathana Energy PCL
    "IP.BK",  # Inter Pharma PCL
    "ASEFA.BK",  # Asefa PCL
    "SITHAI.BK",  # Srithai Superware PCL
    "PHG.BK",  # Patrangsit Healthcare Group PCL
    "POLY.BK",  # Polynet PCL
    "GJS.BK",  # G J Steel PCL
    "ITEL.BK",  # Interlink Telecom PCL
    "QHBREIT.BK",  # Quality Houses Business Complex Leasehold Real Estate Investment Trust
    "UNIQ.BK",  # Unique Engineering and Construction PCL
    "SYNTEC.BK",  # Syntec Construction PCL
    "NTV.BK",  # Nonthavej Hospital PCL
    "BRR.BK",  # Buriram Sugar PCL
    "QHHRREIT.BK",  # Quality Houses Hotel And Residence Freehold And Leasehold Reit
    "HPF.BK",  # Hemaraj Industrial Property and Leasehold Fund
    "IT.BK",  # IT City PCL
    "CMAN.BK",  # Chememan PCL
    "S11.BK",  # S 11 Group PCL
    "PIS.BK",  # Pro Inside PCL
    "PYLON.BK",  # Pylon PCL
    "GROREIT.BK",  # Grande Royal Orchid Hospitality Real Estate Investment Trust
    "MFC.BK",  # MFC Asset Management PCL
    "GABLE.BK",  # G-Able PCL
    "SYMC.BK",  # Symphony Communication PCL
    "NTF.BK",  # NTF Intergroup (Thailand) PCL
    "CTW.BK",  # Charoong Thai Wire and Cable PCL
    "SNC.BK",  # SNC Former PCL
    "MFEC.BK",  # MFEC PCL
    "AMATAR.BK",  # Amata Summit Growth Freehold and Leasehold Real Estate Investment Trus
    "HFT.BK",  # Hwa Fong Rubber (Thailand) PCL
    "TGE.BK",  # Thachang Green Energy PCL
    "ILINK.BK",  # Interlink Communication PCL
    "GRAMMY.BK",  # GMM Grammy PCL
    "RPH.BK",  # Ratchaphruek Hospital PCL
    "RABBIT.BK",  # Rabbit Holdings PCL
    "TC.BK",  # Tropical Canning (Thailand) PCL
    "MASTER.BK",  # Master Style PCL
    "LPH.BK",  # Ladprao General Hospital PCL
    "SCP.BK",  # Southern Concrete Pile PCL
    "TEAMG.BK",  # TEAM Consulting Engineering and Management PCL
    "SEAOIL.BK",  # Sea Oil PCL
    "FPI.BK",  # Fortune Parts Industry PCL
    "TTT.BK",  # Toray Textiles (Thailand) PCL
    "SENA.BK",  # Sena Development PCL
    "BLC.BK",  # Bangkok Lab And Cosmetic PCL
    "A.BK",  # Areeya Property PCL
    "GC.BK",  # Global Connections PCL
    "NOBLE.BK",  # Noble Development PCL
    "ATLAS.BK",  # Atlas Energy PCL
    "TRU.BK",  # Thai Rung Union Car PCL
    "CSC.BK",  # Crown Seal PCL
    "INET.BK",  # Internet Thailand PCL
    "TL.BK",  # Techlead Next PCL
    "SEAFCO.BK",  # Seafco PCL
    "AMATAV.BK",  # Amata VN PCL
    "SFLEX.BK",  # Starflex PCL
    "AIE.BK",  # AI Energy PCL
    "IRC.BK",  # Inoue Rubber (Thailand) PCL
    "MAGURO.BK",  # Maguro Group PCL
    "MONO.BK",  # Mono Next PCL
    "SWC.BK",  # Sherwood Corporation (Thailand) PCL
    "TNP.BK",  # Thanapiriya PCL
    "AUCT.BK",  # Union Auction PCL
    "NAM.BK",  # Namwiwat Medical Corporation PCL
    "TWPC.BK",  # Thai Wah PCL
    "NETBAY.BK",  # Netbay PCL
    "AI.BK",  # Asian Insulators PCL
    "TMW.BK",  # Thai Mitsuwa PCL
    "SUSCO.BK",  # Susco PCL
    "DEMCO.BK",  # Demco PCL
    "BEYOND.BK",  # Bound and Beyond PCL
    "SO.BK",  # Siamrajathanee PCL
    "2S.BK",  # 2S Metal PCL
    "CGH.BK",  # Country Group Holdings PCL
    "BYD.BK",  # Beyond Securities PCL
    "CPNCG.BK",  # CPN Commercial Growth Leasehold Property Fund
    "PAP.BK",  # Pacific Pipe PCL
    "LPN.BK",  # L.P.N. Development PCL
    "LEE.BK",  # Lee Feed Mill PCL
    "CPI.BK",  # Chumporn Palm Oil Industry PCL
    "KTBSTMR.BK",  # KTBST Mixed Freehold and Leasehold Real Estate Investment Trust
    "TK.BK",  # Thitikorn PCL
    "MALEE.BK",  # Malee Group PCL
    "UPOIC.BK",  # United Palm Oil Industry PCL
    "SVOA.BK",  # SVOA PCL
    "ALPHAX.BK",  # Alpha Divisions PCL
    "SPTX.BK",  # SPT X PCL
    "A5.BK",  # Asset Five Group PCL
    "MSC.BK",  # Metro Systems Corporation PCL
    "AJ.BK",  # A.J. Plast PCL
    "WICE.BK",  # Wice Logistics PCL
    "ALT.BK",  # ALT Telecom PCL
    "THIP.BK",  # Thantawan Industry PCL
    "AMARIN.BK",  # Amarin Corporations PCL
    "UBE.BK",  # Ubon Bio Ethanol PCL
    "PRTR.BK",  # PRTR Group PCL
    "OKJ.BK",  # Pluk Phak Praw Rak Mae PCL
    "KISS.BK",  # Rojukiss International PCL
    "NKT.BK",  # Nakornthon Hospital PCL
    "AMA.BK",  # Ama Marine PCL
    "APURE.BK",  # Agripure Holdings PCL
    "MJLF.BK",  # Major Cineplex Lifestyle Leasehold Property Fund
    "SMIT.BK",  # Sahamit Machinery PCL
    "BRI.BK",  # Britania PCL
    "SPRIME.BK",  # S Prime Growth Leasehold Real Estate Investment Trust
    "LUXF.BK",  # Luxury Real Estate Investment Fund
    "AHC.BK",  # Aikchol Hospital PCL
    "EURO.BK",  # Euro Creations PCL
    "WP.BK",  # WP Energy PCL
    "WACOAL.BK",  # Thai Wacoal PCL
    "SAMTEL.BK",  # Samart Telcoms PCL
    "UV.BK",  # Univentures PCL
    "SELIC.BK",  # Selic Corp PCL
    "THRE.BK",  # Thai Reinsurance PCL
    "ITD.BK",  # Italian-Thai Development PCL
    "BR.BK",  # Bangkok Ranch PCL
    "SUN.BK",  # Sunsweet PCL
    "CNT.BK",  # Christiani & Nielsen (Thai) PCL
    "SNPS.BK",  # Specialty Natural Products PCL
    "PRIN.BK",  # Prinsiri PCL
    "QTC.BK",  # QTC Energy PCL
    "UAC.BK",  # UAC Global PCL
    "ASIA.BK",  # Asia Hotel PCL
    "FTE.BK",  # Firetrade Engineering PCL
    "HYDROGEN.BK",  # Hydrogen Freehold and Leasehold Real Estate Investment Trust
    "AGE.BK",  # Asia Green Energy PCL
    "KCC.BK",  # Knight Club Capital Holding PCL
    "ASAP.BK",  # Synergetic Auto Performance PCL
    "KWC.BK",  # Krungdhep Sophon PCL
    "CHAYO.BK",  # Chayo Group PCL
    "ZEN.BK",  # ZEN Corporation Group PCL
    "KDH.BK",  # Thonburi Medical Centre PCL
    "SAFE.BK",  # Safe Fertility Group PCL
    "MDX.BK",  # MDX PCL
    "YUASA.BK",  # Yuasa Battery (Thailand) PCL
    "ML.BK",  # Mida Leasing PCL
    "BWG.BK",  # Better World Green PCL
    "DDD.BK",  # Do Day Dream PCL
    "LTMH.BK",  # LTMH PCL
    "ETC.BK",  # Earth Tech Environment PCL
    "TSE.BK",  # Thai Solar Energy PCL
    "HTECH.BK",  # Halcyon Technology PCL
    "APCO.BK",  # Asian Phytoceuticals PCL
    "CPW.BK",  # Copperwired PCL
    "SPVI.BK",  # S P V I PCL
    "KJL.BK",  # Kijcharoen Engineering Electric PCL
    "TAE.BK",  # Thai Agro Energy PCL
    "SICT.BK",  # Silicon Craft Technology PCL
    "ARROW.BK",  # Arrow Syndicate PCL
    "NVD.BK",  # Nirvana Development PCL
    "BTC.BK",  # The Brooker Group PCL
    "WORK.BK",  # Workpoint Entertainment PCL
    "PACO.BK",  # President Automobile Industries PCL
    "CTARAF.BK",  # Centara Hotels and Resorts Leasehold Property Fund
    "SSSC.BK",  # Siam Steel Service Center PCL
    "UKEM.BK",  # Union Petrochemical PCL
    "ICN.BK",  # Information and Communication Networks PCL
    "SAAM.BK",  # SAAM Development PCL
    "BE8.BK",  # Beryl 8 Plus PCL
    "VRANDA.BK",  # Veranda Resort PCL
    "TPBI.BK",  # TPBI PCL
    "CSR.BK",  # City Sports and Recreation PCL
    "LHRREIT.BK",  # Land And Houses Residential Freehold And Leasehold Real Estate Investm
    "UNIX.BK",  # Unique Plastic Industry PCL
    "UMS.BK",  # Unique Mining Services PCL
    "TQR.BK",  # TQR PCL
    "AKR.BK",  # Ekarat Engineering PCL
    "SRIPANWA.BK",  # Sri panwa Hospitality Real Estate Investment Trust
    "HL.BK",  # Healthlead PCL
    "SSF.BK",  # Surapon Foods PCL
    "GYT.BK",  # Goodyear (Thailand) PCL
    "WINNER.BK",  # Winner Group Enterprise PCL
    "JR.BK",  # J.R.W. Utility PCL
    "LHK.BK",  # Lohakit Metal PCL
    "MICRO.BK",  # Micro Leasing PCL
    "TRP.BK",  # Aesthetic Connect PCL
    "JPARK.BK",  # Jenkongklai PCL
    "MODERN.BK",  # Modernform Group PCL
    "JUBILE.BK",  # Jubilee Enterprise PCL
    "NFC.BK",  # NFC PCL
    "FE.BK",  # Far East Fame Line PCL
    "WHABT.BK",  # WHA Business Complex Freehold and Leasehold Real Estate Investment Tru
    "CFRESH.BK",  # Seafresh Industry PCL
    "SECURE.BK",  # nForce Secure PCL
    "TTI.BK",  # Thai Textile Industry PCL
    "WASH.BK",  # Laundry You PCL
    "ORN.BK",  # Ornsirin Holding PCL
    "ANAN.BK",  # Ananda Development PCL
    "AMARC.BK",  # Asia Medical and Agricultural Laboratory and Research Center PCL
    "BKGI.BK",  # Bangkok Genomics Innovation PCL
    "TTLPF.BK",  # Talaad Thai Leasehold Property Fund
    "TPS.BK",  # The Practical Solution PCL
    "BJCHI.BK",  # BJC Heavy Industries PCL
    "POWER.BK",  # Power Solution Technologies PCL
    "J.BK",  # JAS Asset PCL
    "DTCENT.BK",  # D.T.C. Enterprise PCL
    "EAST.BK",  # Eastern Commercial Leasing PCL
    "KCAR.BK",  # Krungthai Car Rent and Lease PCL
    "BKD.BK",  # Bangkok Dec-Con PCL
    "VCOM.BK",  # Vintcom Technology PCL
    "STP.BK",  # Sahathai Printing & Packaging PCL
    "JDF.BK",  # JD Food PCL
    "CSS.BK",  # Communication & System Solution PCL
    "TAN.BK",  # Tanachira Retail Corporation PCL
    "ESTAR.BK",  # Eastern Star Real Estate PCL
    "MIDA.BK",  # Mida Assets PCL
    "BROCK.BK",  # Baan Rock Garden PCL
    "PJW.BK",  # Panjawattana Plastic PCL
    "HARN.BK",  # Harn Engineering Solutions PCL
    "CH.BK",  # Chin Huay PCL
    "AMC.BK",  # Asia Metal PCL
    "CHAO.BK",  # Chaosua Foods Industry PCL
    "FSX.BK",  # Finansia X PCL
    "BIG.BK",  # Big Camera Corporation PCL
    "PRI.BK",  # Primo Service Solutions PCL
    "AS.BK",  # Asphere Innovations PCL
    "JCT.BK",  # Jack Chia Industries (Thailand) PCL
    "ROH.BK",  # Royal Orchid Hotel (Thailand) PCL
    "MGI.BK",  # Miss Grand International PCL
    "PROUD.BK",  # Proud Real Estate PCL
    "SPREME.BK",  # Supreme Distribution PCL
    "SONIC.BK",  # Sonic Interfreight PCL
    "MII.BK",  # MFC Industrial Investment Property and Leasehold Fund
    "EP.BK",  # Eastern Power Group PCL
    "SORKON.BK",  # S. Khonkaen Foods PCL
    "IROYAL.BK",  # Interroyal Engineering PCL
    "PREB.BK",  # Pre-Built PCL
    "GPI.BK",  # Grand Prix International PCL
    "TPCS.BK",  # TPCS PCL
    "TMILL.BK",  # T S Flour Mill PCL
    "SUTHA.BK",  # Golden Lime PCL
    "STARM.BK",  # Star Money PCL
    "ZAA.BK",  # ZALEKTA PCL
    "D.BK",  # Dental Corporation PCL
    "SDC.BK",  # Samart Digital PCL
    "STI.BK",  # Stonehenge Inter PCL
    "MMM.BK",  # Mmm Capital PCL
    "KIAT.BK",  # Kiattana Transport PCL
    "BEAUTY.BK",  # Beauty Community PCL
    "WIIK.BK",  # WIIK PCL
    "SIRIPRT.BK",  # Siripinyo Real Estate Investment Trust
    "TYCN.BK",  # Tycoons Worldwide Group (Thailand) PCL
    "SINO.BK",  # Sino Logistics Corporation PCL
    "PDG.BK",  # Prodigy PCL
    "VL.BK",  # V.L. Enterprise PCL
    "FMT.BK",  # Fine Metal Technologies PCL
    "NEW.BK",  # Wattana Karnpaet PCL
    "NKI.BK",  # The Navakij Insurance PCL
    "MUD.BK",  # Mud & Hound PCL
    "TPL.BK",  # Thai Parcels PCL
    "PQS.BK",  # Premier Quality Starch PCL
    "PMTA.BK",  # PM Thoresen Asia Holdings PCL
    "MGT.BK",  # Megachem (Thailand) PCL
    "IFS.BK",  # IFS Capital (Thailand) PCL
    "SVT.BK",  # Sun Vending Technology PCL
    "CHASE.BK",  # Chase Asia PCL
    "AMANAH.BK",  # Amanah Leasing PCL
    "KUMWEL.BK",  # Kumwell Corporation PCL
    "CPT.BK",  # CPT Drives and Power PCL
    "PICO.BK",  # Pico (Thailand) PCL
    "NTSC.BK",  # Nutrition SC PCL
    "THE.BK",  # The Steel PCL
    "PATO.BK",  # Pato Chemical Industry PCL
    "SSTRT.BK",  # Sub Sri Thai Real Estate Investment Trust
    "MADAME.BK",  # Madame Bioscience PCL
    "IHL.BK",  # Interhides PCL
    "ADB.BK",  # Applied DB PCL
    "STECH.BK",  # Siam Technic Concrete PCL
    "SALEE.BK",  # Salee Industry PCL
    "BIOTEC.BK",  # Bio Green Energy Tech PCL
    "MPJ.BK",  # MPJ Logistics PCL
    "XBIO.BK",  # X Bioscience PCL
    "TLHPF.BK",  # Thailand Hospitality Property Fund
    "PIMO.BK",  # Pioneer Motor PCL
    "TFI.BK",  # Thai Future Incorporation PCL
    "PPM.BK",  # Porn Prom Metal PCL
    "SENX.BK",  # SEN X PCL
    "APP.BK",  # Applicad PCL
    "NDR.BK",  # N.D. Rubber PCL
    "MITSIB.BK",  # Mitsib Leasing PCL
    "TRUBB.BK",  # Thai Rubber Latex Group PCL
    "DCON.BK",  # Dcon Products PCL
    "88TH.BK",  # 88(Thailand) PCL
    "CCP.BK",  # Chonburi Concrete Product PCL
    "PL.BK",  # Phatra Leasing PCL
    "TOPP.BK",  # Thai O.P.P. PCL
    "F_D.BK",  # Food and Drinks PCL
    "APCS.BK",  # Asia Precision PCL
    "MK.BK",  # M.K. Real Estate Development PCL
    "FTI.BK",  # Function International PCL
    "PLUS.BK",  # Royal Plus PCL
    "MOONG.BK",  # Moong Pattana International PCL
    "BM.BK",  # Bangkok Sheet Metal PCL
    "WARRIX.BK",  # Warrix Sport PCL
    "TRC.BK",  # TRC Construction PCL
    "UREKA.BK",  # Eureka Design PCL
    "UMI.BK",  # The Union Mosaic Industry PCL
    "CGD.BK",  # Country Group Development PCL
    "SIMAT.BK",  # Simat Technologies PCL
    "IMH.BK",  # Intermedical Care and Lab Hospital PCL
    "BVG.BK",  # BlueVenture Group PCL
    "PEACE.BK",  # Peace & Living PCL
    "BSBM.BK",  # Bangsaphan Barmill PCL
    "GTB.BK",  # Getabec PCL
    "GBX.BK",  # Globlex Holding Management PCL
    "BIS.BK",  # Bioscience Animal Health PCL
    "MTW.BK",  # Make To Win Holding PCL
    "UBA.BK",  # Utility Business Alliance PCL
    "NATION.BK",  # Nation Group (Thailand) PCL
    "RSP.BK",  # Rich Sport PCL
    "APO.BK",  # Asian Palm Oil PCL
    "SCI.BK",  # SCI Electric PCL
    "AJA.BK",  # AJ Advance Technology PCL
    "ZIGA.BK",  # Ziga Innovation PCL
    "CAZ.BK",  # CAZ (Thailand) PCL
    "NUT.BK",  # Nutrition Profess PCL
    "FVC.BK",  # Filter Vision PCL
    "LTS.BK",  # Light Up Total Solution PCL
    "PHOL.BK",  # Phol Dhanya PCL
    "BUI.BK",  # Bangkok Union Insurance PCL
    "EASON.BK",  # Eason & Co PCL
    "GAHREIT.BK",  # Grande Hospitality Real Estate Investment Trust
    "ALLA.BK",  # Alla PCL
    "CIVIL.BK",  # Civil Engineering PCL
    "NOVA.BK",  # Nova Empire PCL
    "GREEN.BK",  # Green Resources PCL
    "KOOL.BK",  # CL Venture PCL
    "WINDOW.BK",  # Window Asia PCL
    "UP.BK",  # Union Plastic PCL
    "ADD.BK",  # AddTech Hub PCL
    "SMART.BK",  # Smart Concrete PCL
    "PG.BK",  # People's Garment PCL
    "ISSARA.BK",  # Issara Real Estate Investment Trust
    "MATCH.BK",  # Matching Maximize Solution PCL
    "THREL.BK",  # Thaire Life Assurance PCL
    "SFT.BK",  # Shrinkflex (Thailand) PCL
    "AF.BK",  # AIRA Factoring PCL
    "PRAKIT.BK",  # Prakit Holdings PCL
    "LEO.BK",  # Leo Global Logistics PCL
    "INSURE.BK",  # Indara Insurance PCL
    "COLOR.BK",  # Salee Colour PCL
    "MENA.BK",  # Mena Transport PCL
    "OCC.BK",  # O.C.C. PCL
    "CM.BK",  # Chiangmai Frozen Foods PCL
    "AQUA.BK",  # Aqua Corporation PCL
    "MANRIN.BK",  # Mandarin Hotel PCL
    "L_E.BK",  # Lighting and Equipment PCL
    "ACC.BK",  # Advanced Connection Corporation PCL
    "SLP.BK",  # Salee Printing PCL
    "MATI.BK",  # Matichon PCL
    "TEKA.BK",  # Teka Construction PCL
    "PDJ.BK",  # Pranda Jewelry PCL
    "TNITY.BK",  # Trinity Watthana PCL
    "CWT.BK",  # Chai Watana Tannery Group PCL
    "NCH.BK",  # N.C. Housing PCL
    "NAT.BK",  # NAT Absolute Technologies PCL
    "MASTEC.BK",  # Masstec Link PCL
    "SPACK.BK",  # S. Pack & Print PCL
    "CPR.BK",  # CPR Gomu Industrial PCL
    "SAMCO.BK",  # Sammakorn PCL
    "SST.BK",  # Sub Sri Thai PCL
    "SSPF.BK",  # Sala @ Sathorn Property Fund
    "ATP30.BK",  # ATP 30 PCL
    "RML.BK",  # Raimon Land PCL
    "CHOTI.BK",  # Kiang Huat Sea Gull Trading Frozen Food PCL
    "PLT.BK",  # Pilatus Marine PCL
    "MORE.BK",  # More Return PCL
    "ABM.BK",  # Asia Biomass PCL
    "SCN.BK",  # Scan Inter PCL
    "AIMCG.BK",  # AIM Commercial Growth Freehold And Leasehold Real Estate Investment Tr
    "TH.BK",  # Tong Hua Holding PCL
    "PORT.BK",  # Sahathai Terminal PCL
    "FLOYD.BK",  # Floyd PCL
    "PAF.BK",  # Pan Asia Footwear PCL
    "TPCH.BK",  # TPC Power Holding PCL
    "CFARM.BK",  # Chuwit Farm (2019) PCL
    "GFC.BK",  # Genesis Fertility Center PCL
    "YONG.BK",  # Yong Concrete PCL
    "K.BK",  # Kingsmen C.M.T.I. PCL
    "XYZ.BK",  # RSXYZ PCL
    "HANN.BK",  # Mukdahan International Hospital PCL
    "RPC.BK",  # RPCG PCL
    "SIAM.BK",  # Siam Steel International PCL
    "TPP.BK",  # Thai Packaging & Printing PCL
    "DEXON.BK",  # Dexon Technology PCL
    "FN.BK",  # FN Factory Outlet PCL
    "WAVE.BK",  # Wave Exponential PCL
    "JCK.BK",  # JCK International PCL
    "ACG.BK",  # Autocorp Holding PCL
    "CMC.BK",  # Chaoprayamahanakorn PCL
    "DOD.BK",  # DOD Biotech PCL
    "WFX.BK",  # World Flex PCL
    "KUN.BK",  # Villa Kunalai PCL
    "NEP.BK",  # NEP Realty and Industry PCL
    "EFORL.BK",  # E for L Aim PCL
    "CEN.BK",  # Capital Engineering Network PCL
    "THANA.BK",  # Thanasiri Group PCL
    "TRITN.BK",  # Triton Holding PCL
    "VPO.BK",  # Vichitbhan Palmoil PCL
    "CPH.BK",  # Castle Peak Holdings PCL
    "VARO.BK",  # Varopakorn PCL
    "UEC.BK",  # Unimit Engineering PCL
    "TCC.BK",  # Thai Capital Corporation PCL
    "WGE.BK",  # Well Graded Engineering PCL
    "MBAX.BK",  # Multibax PCL
    "CHIC.BK",  # Chic Republic PCL
    "KWM.BK",  # K.W. Metal Work PCL
    "PF.BK",  # Property Perfect PCL
    "TATG.BK",  # Thai Auto Tools and Die PCL
    "RT.BK",  # Right Tunnelling PCL
    "SCL.BK",  # S.C.L Motor Part PCL
    "GTV.BK",  # Green Tech Ventures PCL
    "UBIS.BK",  # Ubis (Asia) PCL
    "CI.BK",  # Charn Issara Development PCL
    "SRS.BK",  # Sirisoft PCL
    "WINMED.BK",  # Winnergy Medical PCL
    "PMC.BK",  # PMC Label Materials PCL
    "GENCO.BK",  # General Environmental Conservation PCL
    "CITY.BK",  # City Steel PCL
    "TBSP.BK",  # TBSP PCL
    "TRV.BK",  # T.R.V. Rubber Products PCL
    "ITNS.BK",  # International Network System PCL
    "SE.BK",  # SiamEast Solutions PCL
    "READY.BK",  # Readyplanet PCL
    "PLANET.BK",  # Planet Communications Asia PCL
    "ASIMAR.BK",  # Asian Marine Services PCL
    "JAK.BK",  # Jakpaisan Estate PCL
    "SANKO.BK",  # Sanko Diecasting (Thailand) PCL
    "KPNREIT.BK",  # KPN Freehold and Leasehold Real Estate Investment Trust
    "STC.BK",  # STC Concrete Product PCL
    "TBN.BK",  # TBN Corporation PCL
    "KTMS.BK",  # KT Medical Service PCL
    "PROEN.BK",  # PROEN Corp PCL
    "PRAPAT.BK",  # Peerapat Technology PCL
    "GEL.BK",  # General Engineering PCL
    "EVER.BK",  # Everland PCL
    "NV.BK",  # Nova Organic PCL
    "IVF.BK",  # Inspire IVF PCL
    "ITTHI.BK",  # Itthirit Nice Corporation PCL
    "CEYE.BK",  # Chamni's Eye PCL
    "NRF.BK",  # NR Instant Produce PCL
    "MOTHER.BK",  # Mother Marketing PCL
    "LIT.BK",  # Lease IT PCL
    "TWP.BK",  # Thai Wire Products PCL
    "ETE.BK",  # Eastern Technical Engineering PCL
    "TAKUNI.BK",  # Takuni Group PCL
    "CPL.BK",  # CPL Group PCL
    "NL.BK",  # NL Development PCL
    "ONSENS.BK",  # Onsen Retreat and Spa Group PCL
    "TMC.BK",  # T.M.C. Industrial PCL
    "TNDT.BK",  # Thai Nondestructive Testing PCL
    "BC.BK",  # Boutique Corporation PCL
    "SR.BK",  # Siamraj PCL
    "TPA.BK",  # Thai Poly Acrylic PCL
    "TPLAS.BK",  # Thai Plastic Industrial (1994) PCL
    "TMI.BK",  # Teera-Mongkol Industry PCL
    "TNPC.BK",  # Thai Nam Plastic PCL
    "I2.BK",  # I2 Enterprise PCL
    "TERA.BK",  # Terabyte Plus PCL
    "SEI.BK",  # SEI Medical PCL
    "IND.BK",  # Index International Group PCL
    "MCA.BK",  # Market Connections Asia PCL
    "TM.BK",  # Techno Medical PCL
    "SOLAR.BK",  # Solartron PCL
    "MJD.BK",  # Major Development PCL
    "CMO.BK",  # CMO PCL
    "AKP.BK",  # Akkhie Prakarn PCL
    "GLORY.BK",  # Glory Forever PCL
    "ARIN.BK",  # Arinsiri Land PCL
    "TCOAT.BK",  # Thai Coating Industrial PCL
    "B52.BK",  # B-52 Capital PCL
    "STX.BK",  # Stone One PCL
    "NC.BK",  # Newcity (Bangkok) PCL
    "FNS.BK",  # FNS Holdings PCL
    "TCJ.BK",  # T.C.J. Asia PCL
    "RS.BK",  # RS PCL
    "RICHY.BK",  # Richy Place 2002 PCL
    "ETL.BK",  # Euroasia Total Logistics PCL
    "CSP.BK",  # CSP Steel Center PCL
    "BPS.BK",  # BPS Technology PCL
    "PRIME.BK",  # Prime Road Power PCL
    "DHOUSE.BK",  # Dhouse Pattana PCL
    "EMC.BK",  # EMC PCL
    "CRANE.BK",  # Chukai PCL
    "TKT.BK",  # T.Krungthai Industries PCL
    "PK.BK",  # Patkol PCL
    "B.BK",  # Begistics PCL
    "SK.BK",  # Sirakorn PCL
    "SMD100.BK",  # SMD Rise PCL
    "CHARAN.BK",  # Charan Insurance PCL
    "PTC.BK",  # Premier Tank Corporation PCL
    "KK.BK",  # K&K Superstore Southern PCL
    "CRD.BK",  # Chiangmai Rimdoi PCL
    "TCMC.BK",  # TCM Corporation PCL
    "AMR.BK",  # AMR Asia PCL
    "PANEL.BK",  # Panelesmatic Solutions PCL
    "BLESS.BK",  # Bless Asset Group PCL
    "AFC.BK",  # Asia Fiber PCL
    "MNRF.BK",  # MFC Multi-National Residence Fund
    "ROCK.BK",  # Rockworth PCL
    "PPPM.BK",  # PP Prime PCL
    "ARIP.BK",  # ARIP PCL
    "CHEWA.BK",  # Chewathai PCL
    "PPP.BK",  # Premier Products PCL
    "TIGER.BK",  # Thai Enger Holding PCL
    "TVT.BK",  # TV Thunder PCL
    "TWZ.BK",  # TWZ Corporation PCL
    "QLT.BK",  # Qualitech PCL
    "SGF.BK",  # SGF Capital PCL
    "SQ.BK",  # Sahakol Equipment PCL
    "CPANEL.BK",  # CPanel PCL
    "OGC.BK",  # Ocean Glass PCL
    "NCP.BK",  # Nice Call PCL
    "SKE.BK",  # Sakol Energy PCL
    "GRAND.BK",  # Grande Asset Hotels and Property PCL
    "PERM.BK",  # Permsin Steel Works PCL
    "KCM.BK",  # K.C. Metalsheet PCL
    "SVR.BK",  # Sivarom Real Estate PCL
    "ASN.BK",  # ASN Broker PCL
    "IRCP.BK",  # International Research Corporation PCL
    "IIG.BK",  # I&I Group PCL
    "KASET.BK",  # Thai Ha PCL
    "BKA.BK",  # Bangkok Asset Intergroup PCL
    "BTNC.BK",  # Boutique Newcity PCL
    "DTCI.BK",  # D.T.C. Industries PCL
    "UPF.BK",  # Union Pioneer PCL
    "WIN.BK",  # Wyncoast Industrial Park PCL
    "STOWER.BK",  # Sky Tower PCL
    "DIMET.BK",  # Dimet (Siam) PCL
    "VIBE.BK",  # Vibe Synergy Group PCL
    "EMPIRE.BK",  # Origin Global Empire PCL
    "RWI.BK",  # Rayong Wire Industries PCL
    "PLE.BK",  # Power Line Engineering PCL
    "TNPF.BK",  # Trinity Freehold and Leasehold Property Fund
    "FANCY.BK",  # Fancy Wood Industries PCL
    "BSM.BK",  # BuilderSmart PCL
    "PPS.BK",  # Project Planning Service PCL
    "SAWANG.BK",  # Sawang Export PCL
    "LDC.BK",  # LDC Dental PCL
    "TGPRO.BK",  # Thai-German Products PCL
    "PRECHA.BK",  # Preecha Group PCL
    "NPK.BK",  # New Plus Knitting PCL
    "RP.BK",  # Raja Ferry Port PCL
    "BGT.BK",  # BGT Corporation PCL
    "INGRS.BK",  # Ingress Industrial (Thailand) PCL
    "GCAP.BK",  # G Capital PCL
    "THMUI.BK",  # Thai Mui Corporation PCL
    "ECF.BK",  # East Coast Furnitech PCL
    "IDG.BK",  # Indigy PCL
    "SKIN.BK",  # Skin Laboratory PCL
    "HYDRO.BK",  # Hydrotek PCL
    "KWI.BK",  # KWI PCL
    "SAF.BK",  # S.A.F. Special Steel PCL
    "CIG.BK",  # C.I. Group PCL
    "YGG.BK",  # Yggdrazil Group PCL
    "SCM.BK",  # Successmore Being PCL
    "TVDH.BK",  # TVD Holdings PCL
    "SAM.BK",  # Samchai Steel Industries PCL
    "KC.BK",  # K.C. Property PCL
    "NWR.BK",  # Nawarat Patanakarn PCL
    "PROS.BK",  # Prosper Engineering PCL
    "NCL.BK",  # NCL International Logistics PCL
    "TSI.BK",  # The Thai Setakij Insurance PCL
    "MILL.BK",  # Millcon Steel PCL
    "HPT.BK",  # Home Pottery PCL
    "COMAN.BK",  # Comanche International PCL
    "PEER.BK",  # Peer For You PCL
    "QTCG.BK",  # QTCG PCL
    "WSOL.BK",  # WSOL PCL
    "VS.BK",  # Viserve Enterprise PCL
    "META.BK",  # Meta Corporation PCL
    "BTW.BK",  # BT Wealth Industries PCL
    "TPOLY.BK",  # Thai Polycons PCL
    "DPAINT.BK",  # Delta Paint PCL
    "TTCL.BK",  # TTCL PCL
    "AKS.BK",  # AKS Corporation PCL
    "CV.BK",  # Clover Power PCL
    "TSR.BK",  # TSR Living Solution PCL
    "QDC.BK",  # Quantum D C PCL
    "MVP.BK",  # M Vision PCL
    "CHO.BK",  # Cho Thavee PCL
]
