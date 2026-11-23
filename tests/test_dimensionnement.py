import math
import unittest
from tools.dimensionnement import calcul


class DimensionnementTests(unittest.TestCase):
    def test_veille_et_conso_propre(self):
        r = calcul(clips=0)
        self.assertAlmostEqual(r['charge_usb_wh_j'], 0.6)
        self.assertAlmostEqual(r['propre_wh_j'], 0.624)
        self.assertAlmostEqual(r['besoin_cellule_wh_j'], 0.6 / 0.85 + 0.624)
        self.assertAlmostEqual(r['reserve_wh'], 19.296)

    def test_journee_active_sans_double_compte(self):
        r = calcul(clips=1, duree_s=86400, latence_s=0, actif_ma=140)
        self.assertAlmostEqual(r['charge_usb_wh_j'], 16.8)

    def test_latence_comptee(self):
        r = calcul(clips=100)
        self.assertEqual(r['actif_s_j'], 2300)
        self.assertAlmostEqual(r['charge_usb_wh_j'], 1.7020833333333334)

    def test_seuil_solaire(self):
        r = calcul()
        self.assertAlmostEqual(calcul(hsp=r['hsp_min'])['bilan_wh_j'], 0)
        self.assertIsNone(calcul(hsp=24)['jours_avant_reserve_epuisee'])

    def test_ombre_totale_et_panneau_nul(self):
        for options in ({'ombre': 0}, {'panneau_w': 0}):
            r = calcul(**options)
            self.assertIsNone(r['hsp_min'])
            self.assertEqual(r['jours_avant_reserve_epuisee'], r['jours_sans_soleil'])

    def test_sensibilite(self):
        self.assertGreater(calcul(clips=500)['besoin_cellule_wh_j'], calcul(clips=10)['besoin_cellule_wh_j'])
        self.assertAlmostEqual(calcul(ombre=0.5)['hsp_min'], 2 * calcul()['hsp_min'])
        self.assertGreater(calcul(propre_w=0.05)['besoin_cellule_wh_j'], calcul()['besoin_cellule_wh_j'])

    def test_sans_consommation(self):
        r = calcul(clips=0, veille_ma=0, propre_w=0)
        self.assertIsNone(r['jours_sans_soleil'])
        self.assertEqual(r['hsp_min'], 0)

    def test_entrees_invalides(self):
        for options in ({'clips': -1}, {'clips': 1.5}, {'clips': 4000},
                        {'hsp': 25}, {'ombre': 1.01}, {'veille_ma': math.nan},
                        {'propre_w': math.inf}, {'rendement_usb': 0},
                        {'fraction_utile': 1.1}, {'rendement_solaire': -1}):
            with self.subTest(options=options), self.assertRaises(ValueError):
                calcul(**options)


if __name__ == '__main__':
    unittest.main()
