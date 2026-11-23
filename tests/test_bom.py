import unittest
from decimal import Decimal

from tools import bom


class BomTests(unittest.TestCase):
    def setUp(self):
        self.lignes = bom.lire()

    def test_partie_generee_a_jour(self):
        texte = bom.MD.read_text(encoding='utf-8')
        i, j = bom.section_actuelle(texte)
        self.assertEqual(texte[i:j], bom.generer(self.lignes))

    def test_totaux_additionnent_les_lignes(self):
        t = bom.totaux(self.lignes)
        self.assertEqual(sum(t.values()), sum(l['prix'] * l['qte'] for l in self.lignes))
        ferme = sum((v for (s, _), v in t.items() if s == 'ferme'), Decimal(0))
        self.assertEqual(ferme, Decimal('301.06'))

    def test_elements_du_readme_presents(self):
        ids = {l['id'] for l in self.lignes if l['statut'] == 'ferme'}
        for requis in ('carte', 'sd', 'led', 'transistor', 'barriere', 'ds18b20',
                       'v75', 'p110', 'rallonge', 'sbu', 'coffret', 'pg7', 'cable'):
            self.assertIn(requis, ids)

    def test_references_gotronic_numeriques(self):
        for l in self.lignes:
            if l['marchand'] == 'Gotronic':
                with self.subTest(l['id']):
                    self.assertTrue(l['reference'].isdigit())
                    self.assertTrue(l['url'].startswith('https://www.gotronic.fr/art-'))

    def test_quatre_led_au_moins(self):
        led = next(l for l in self.lignes if l['id'] == 'led')
        self.assertGreaterEqual(led['qte'], 4)


if __name__ == '__main__':
    unittest.main()
