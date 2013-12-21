import datetime
import base64

def compress(arr):
    compressed = arr[:]
    compressed.append('1')
    compressed.reverse()
    compressed.append('1')
    return str(int(compressed, 2))

# A direct copy of CompressLargeBin()
# Compress in chunks of 50
def compress_large(arr):
    compressed = ''
    for i in range(len(arr)/50):
        compressed += compress(arr[i:i+50])
    compressed += compress(arr[len(arr)/50*50:])
    return compressed

def get_info():
    try:
        cookies = int(raw_input('Enter number of cookies in bank: '))
        cookies_earned = cookies # Or else it detects that you're cheating
        cookie_clicks = 0
        golden_clicks = 0
        handmade_cookies = cookie_clicks
        missed_golden_clicks = 0 # What is this?
        background_type = 0      # And this?
        milk_type = 0            # And this?
        cookies_reset = 0        # And this?
        elder_wrath = 0          # And this?
        pledges = 0              # And this?
        pledgeT = 0              # And this?
        next_research = 0        # And this?
        researchT = 0            # And this?
    except ValueError:
        print "Could not read input."
    info_arr = [cookies, cookies_earned, cookie_clicks, golden_clicks, handmade_cookies,
                missed_golden_clicks, background_type, milk_type, cookies_reset, elder_wrath,
                pledges, pledgeT, next_research, researchT]
    info_arr = map(lambda x: str(x), info_arr)
    info_str = ';'.join(info_arr)
    return info_str

def get_buildings():
    try:
        cursors = int(raw_input('Enter number of cursors: '))
        grandmas = int(raw_input('Enter number of grandmas: '))
        farms = int(raw_input('Enter number of farms: '))
        factories = int(raw_input('Enter number of factories: '))
        mines = int(raw_input('Enter number of mines: '))
        shipments = int(raw_input('Enter number of shipments: '))
        alchemy_labs = int(raw_input('Enter number of alchemy_labs: '))
        portals = int(raw_input('Enter number of portals: '))
        time_machines = int(raw_input('Enter number of time_machines: '))
        antimatter_condensers = int(raw_input('Enter number of antimatter condensers: '))
    except ValueError:
        print "Could not read input."
    buildings_arr = [cursors, grandmas, farms, factories, mines, shipments, alchemy_labs,
                     portals, time_machines, antimatter_condensers]
    buildings_arr = map(lambda x: ','.join([str(x), str(x), str(0), str(0)]), buildings_arr)
    buildings_str = ';'.join(buildings_arr)
    return buildings_str

def break_cookies():
    VERSION = '1.0402' # Current version. Change as necessary
    BUFFER = ''
    START_DATE = datetime.datetime.now().strftime('%s000') # Now
    PREFS = '111111' # Default prefs
    INFO = get_info() # Cookie info
    BUILDINGS = get_buildings()
    UPGRADES = '2251799813685249;2251799813685249;2251799813685249;2251799813685249;524289' # I can guess what this is
    ACHIEVEMENTS = '2251799813685249;8796093022209' # Same with this
    vals = [VERSION, BUFFER, START_DATE, PREFS, INFO, BUILDINGS, UPGRADES, ACHIEVEMENTS]
    vals_str = '|'.join(vals)
    encoded = base64.b64encode(vals_str.decode('utf-8'))
    return encoded

if __name__=='__main__':
    code = break_cookies()
    print '\nImport the following save code: \n'
    print code + '\n'
