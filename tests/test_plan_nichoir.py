import math
import subprocess
import sys
import unittest
from pathlib import Path

from tools import plan_nichoir as p

ROOT = Path(__file__).resolve().parents[1]


class PlanNichoirTests(unittest.TestCase):
    def test_criteres_respectes(self):
        for libelle, ok, detail in p.verifications():
            with self.subTest(libelle):
                self.assertTrue(ok, detail)

    def test_cotes_cles(self):
        self.assertEqual(p.EXT, 180)
        self.assertEqual((p.Z_PLAFOND, p.Z_CLOISON, p.Z_TROU), (250, 270, 190))
        self.assertAlmostEqual(p.H_NORD, 490)
        pieces = {x['nom']: x for x in p.pieces()}
        self.assertAlmostEqual(pieces['Côté sud (porte pivotante)']['h'], 327)
        self.assertEqual(pieces['Côté sud (porte pivotante)']['l'], 138)
        self.assertAlmostEqual(pieces['Côté nord']['h'], 490)

    def test_flan_facade_dos(self):
        # Une coupe à 45° sur 180 de large décale de 180 : deux trapèzes 310/490.
        self.assertAlmostEqual(p.H_NORD - p.H_SUD, p.EXT * math.tan(math.radians(p.PENTE)))
        self.assertEqual(p.debit()['flan_facade_dos'], 805)  # 800 + 3·√2
        self.assertEqual(p.debit()['longueur_planche_180'], 2047)

    def test_pivot_porte_entre_cloison_et_toit(self):
        self.assertTrue(p.Z_CLOISON < p.Z_PIVOT < p.z_toit(0) - p.JEU_PORTE)

    def test_porte_ouverte_degage_le_toit(self):
        # Rotation autour de (x=E/2, z=Z_PIVOT) : le haut de la porte s'écarte du toit.
        xp, zp = p.E / 2, p.Z_PIVOT
        coins = [(0, p.H_SUD - p.JEU_PORTE), (p.E, p.z_toit(p.E) - p.JEU_PORTE)]
        for deg in range(0, 91, 5):
            a = math.radians(deg)
            for x, z in coins:
                # la porte bascule vers l'extérieur par le bas : le haut part vers +x
                xr = xp + (x - xp) * math.cos(a) + (z - zp) * math.sin(a)
                zr = zp - (x - xp) * math.sin(a) + (z - zp) * math.cos(a)
                with self.subTest(deg=deg, coin=(x, z)):
                    self.assertLess(zr, p.z_toit(xr))

    def test_svg_a_jour(self):
        r = subprocess.run([sys.executable, 'tools/plan_nichoir.py', '--check'],
                           cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == '__main__':
    unittest.main()
