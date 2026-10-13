"""
File originally made by Cathy Lefebvre (v 1.2)
Updated for Python 3 & Pyodide compatibility
Extracts pledge and brother preference lists from CSV files titled:
BigListChoices.csv AND LittleListChoices.csv
"""
import csv


class data:
    def __init__(self):
        # 1. Parse BigListChoices.csv
        self.pledgeprefers = {}
        with open("BigListChoices.csv", "r", encoding="utf-8") as pledgeLists:
            pledgeListR = csv.reader(pledgeLists)
            for row in pledgeListR:
                if not row or not any(row):
                    continue
                prefs = []
                for name in row[1:]:
                    name = name.strip()
                    if name and name.lower() != "none":
                        prefs.append(name)
                if prefs:
                    self.pledgeprefers[row[0].strip()] = prefs
        # 2. Parse LittleListChoices.csv
        self.brosprefers = {}
        with open("LittleListChoices.csv", "r", encoding="utf-8") as littleLists:
            broListR = csv.reader(littleLists)
            for row in broListR:
                if not row or not any(row):
                    continue
                prefs = []
                # Check if brother opted in ('Yes')
                if len(row) > 1 and row[1].strip().lower() == "yes":
                    for name in row[2:]:
                        name = name.strip()
                        if name and name.lower() != "none":
                            prefs.append(name)
                self.brosprefers[row[0].strip()] = prefs

        self.pledges = sorted(self.pledgeprefers.keys())
        self.bros = sorted(self.brosprefers.keys())

        print(f"Loaded {len(self.pledgeprefers)} pledges from BigListChoices.csv")
        print(f"Pledges: {list(self.pledgeprefers.keys())}")

        print(f"Loaded {len(self.brosprefers)} brothers from LittleListChoices.csv")
        print(f"Brothers: {list(self.brosprefers.keys())}")

    def getPledges(self):
        return self.pledges

    def getBros(self):
        return self.bros

    def getBroPreferences(self):
        return self.brosprefers

    def getPledgePreferences(self):
        return self.pledgeprefers

    def changePledges(self, bro, old, new):
        broPrefList = self.getPreferenceList(bro)
        if old in broPrefList and new in broPrefList:
            return broPrefList.index(new) < broPrefList.index(old)
        return False

    def preferredPledge(self, bro, pledges):
        broPrefList = self.getPreferenceList(bro)
        pref = None
        for p in pledges:
            if p in broPrefList:
                if pref is None or broPrefList.index(p) < broPrefList.index(pref):
                    pref = p
        return pref

    def getPreferenceList(self, person):
        if person in self.pledgeprefers:
            return self.pledgeprefers[person]
        elif person in self.brosprefers:
            return self.brosprefers[person]
        return []
