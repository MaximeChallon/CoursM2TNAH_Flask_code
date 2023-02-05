from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, TextAreaField, PasswordField

class Recherche(FlaskForm):
    nom_pays = StringField("nom_pays", validators=[]) 
    ressources = SelectField('ressources', choices=[('', ''),('PET', 'pétrole'), ('GOL', 'or')])
    continents = SelectField('ressources', choices=[('', ''),('Europe', 'Europe'), ('Asia', 'Asie'), ('Africa', 'Afrique'), ('Oceania', 'Océanie'), ('North America', 'Amérique du Nord')])

class InsertionPays(FlaskForm):
    code_pays =  StringField("code_pays", validators=[]) 
    nom_pays =  StringField("nom_pays", validators=[])
    type = SelectField('type', choices=[('', ''),('sovereign', 'Souverain'), ('dependency', 'Dépendance'), ('ocean', 'Océan'), ('other', 'Autre')])
    introduction =  TextAreaField("code_pays", validators=[]) 
    ressources = SelectMultipleField('ressources', choices=[('', ''),('PET','petroleum'),('NAT','natural gas'),('IRO','iron ore'),('PHO','phosphates'),('URA','uranium'),('LEA','lead'),('ZIN','zinc'),('DIA','diamonds'),('COP','copper'),('FEL','feldspar'),('GOL','gold'),('BAU','bauxite'),('NIC','nickel'),('SAL','salt'),('SOD','soda ash'),('POT','potash'),('COA','coal'),('SIL','silver'),('LIM','limestone'),('MAR','marble'),('TIM','timber'),('RAR','rare earth oxides'),('PEA','peat'),('COB','cobalt'),('PLA','platinum'),('VAN','vanadium'),('ARA','arable land'),('HYD','hydropower'),('NIO','niobium'),('TAN','tantalum'),('TIN','tin'),('TUN','tungsten'),('KAO','kaolin'),('FIS','fish (Lake Chad)'),('SAN','sand and gravel'),('MAG','magnesium'),('MAN','manganese'),('OIL','oil'),('BAS','basalt rock'),('CLA','clay'),('GYP','gypsum'),('GRA','granite'),('PUM','pumice'),('TAL','talc'),('ASB','asbestos'),('ZIR','zircon'),('RUB','rubber'),('COC','cocoa beans'),('COF','coffee'),('PAL','palm oil'),('GEM','gemstones'),('FLU','fluorspar'),('WIL','wildlife'),('WAT','water'),('BUI','building stone'),('CHR','chromite'),('QUA','quartz'),('TAR','tar sands'),('SEM','semiprecious stones'),('MIC','mica'),('AND','and bauxite'),('NOT','note'),('MOL','molybdenum'),('HAR','hardwoods'),('MET','methane'),('CIN','cinnamon trees'),('ANT','antimony'),('LOB','lobster'),('LIK','likely oil reserves'),('LIT','lithium'),('CAD','cadmium'),('FOR','forests'),('EME','emeralds'),('ICE','icefish'),('TOO','toothfish'),('NON','none'),('CRA','crayfish'),('ALU','alumina'),('MIN','mineral sands'),('OPA','opals'),('BEA','beaches'),('NEG','NEGL'),('GEO','geothermal power'),('TRO','tropical fruit'),('CHI','chicle'),('CAL','calcium carbonate'),('<P>','<p>fish'),('MAH','mahogany forests'),('SHR','shrimp'),('ASP','asphalt'),('SPI','spiny lobster'),('CON','conch'),('PRO','protected harbors'),('HOT','hot springs</p>'),('PLE','pleasant climate'),('MER','mercury'),('BIS','bismuth'),('BRO','brown coal'),('SUL','sulfur'),('PRE','precious stones'),('HEL','helium'),('ARS','arsenic'),('GAL','gallium'),('GER','germanium'),('HAF','hafnium'),('TEL','tellurium'),('SEL','selenium'),('STR','strontium'),('LIG','lignite'),('CAR','carbonates'),('DOL','dolomitic limestone'),('CHA','chalk'),('PYR','pyrites'),('STO','stone'),('BAR','barite'),('SEA','sea mud'),('SOF','soft coal'),('WHA','whales'),('FRE','French Guiana'),('CRO','cropland'),('LOW','low-grade iron ore'),('AMB','amber'),('GAS','gas'),('SEP','sepiolite'),('SLA','slate'),('SHA','shale oil'),('ROC','rock salt'),('BOR','borate'),('PER','perlite'),('BER','beryllium'),('NIT','nitrates'),('SQU','squid'),('SPH','sphagnum moss'),('OTH','other minerals'),('SUG','sugarcane'),('SCE','scenic beauty'),('POO','poor quality coal')])
    continent = SelectField('ressources', choices=[('', ''),('Europe', 'Europe'), ('Asia', 'Asie'), ('Africa', 'Afrique'), ('Oceania', 'Océanie'), ('North America', 'Amérique du Nord')])

class InsertionRessource(FlaskForm):
    code_res =  StringField("code_res", validators=[]) 
    nom_res =  StringField("nom_res", validators=[])

class SuppressionPays(FlaskForm):        
    code_pays =  StringField("code_pays", validators=[]) 
    nom_pays = SelectField("nom_pays", choices=[])

class SuppressionRessource(FlaskForm):        
    code_res =  StringField("code_res", validators=[]) 
    nom_res = SelectField("nom_res", choices=[])

class AjoutUtilisateur(FlaskForm):
    prenom = StringField("prenom", validators=[])
    password = PasswordField("password", validators=[])