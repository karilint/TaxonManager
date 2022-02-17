from django.test import TestCase
from django.utils import timezone
from front.models import (Comment, Expert, ExpertsGeographicDiv, GeographicDiv, Hierarchy, Kingdom, Publication,
                          ReferenceLink, SynonymLink, TaxonAuthorLkp, TaxonomicUnit, TaxonUnitType, TuCommentLink)  # pylint:disable=W0611


class ModelTest(TestCase):
    """
    Test the the existence of objects and relationships between the tables
    """
    @classmethod
    def setUpTestData(cls):
        Kingdom.objects.create(
            kingdom_name="Animalia",
            update_date=timezone.now()
        )
        cls.kingdom = Kingdom.objects.all()[0]

        TaxonUnitType.objects.create(
            kingdom=cls.kingdom,
            rank_id=20,
            rank_name="Subkingdom",
            dir_parent_rank_id=10,
            req_parent_rank_id=10,
            update_date=timezone.now()
        )
        cls.taxon_unit_type = TaxonUnitType.objects.all()[0]

        TaxonAuthorLkp.objects.create(
            taxon_author_id=5656,
            taxon_author="(Linnaeus, 1758)",
            update_date=timezone.now(),
            kingdom=cls.kingdom,
            short_author="Linnaeus 1758"
        )
        cls.author = TaxonAuthorLkp.objects.all()[0]

        TaxonomicUnit.objects.create(
            unit_name1="Lynx",
            taxon_author_id=cls.author,
            parent_tsn=100,
            kingdom=cls.kingdom,
            complete_name="Lynx lynx"
        )

        cls.taxonomic_unit = TaxonomicUnit.objects.all()[0]

    def test_kingdom_exists(self):
        self.assertTrue(isinstance(self.kingdom, Kingdom))

    def test_kingdom_string_method(self):
        self.assertEqual(str(self.kingdom), "Animalia")

    def test_taxon_unit_type_exists(self):
        self.assertTrue(isinstance(self.taxon_unit_type, TaxonUnitType))

    def test_taxon_unit_type_string_method(self):
        self.assertEqual(str(self.taxon_unit_type),
                         "Kingdom: Animalia, rank_name: Subkingdom, rank_id:20")

    def test_taxon_unit_type_refers_to_kingdom_correctly(self):
        self.assertEqual(self.taxon_unit_type.kingdom.kingdom_name, "Animalia")

    def test_taxon_author_lkp_exists(self):
        self.assertTrue(isinstance(self.author, TaxonAuthorLkp))

    def test_taxon_author_string_method(self):
        self.assertEqual(str(self.author), "(Linnaeus, 1758)")
   
    def test_taxon_author_refers_to_kingdom_correctly(self):
        self.assertEqual(self.author.kingdom.kingdom_name, "Animalia")

    def test_taxonomic_unit_exists(self):
        self.assertTrue(isinstance(self.taxonomic_unit, TaxonomicUnit))

    def test_taxonomic_unit_string_method(self):
        self.assertEqual(
            str(self.taxonomic_unit), "Lynx, Kingdom: Animalia (tsn_id: 1, parent_tsn: 100)")

    def test_taxonomic_unit_refers_to_kingdom_correctly(self):
        self.assertEqual(self.taxonomic_unit.kingdom.kingdom_name, "Animalia")

    def test_taxonomic_unit_refers_to_taxon_author_correctly(self):
        self.assertEqual(
            self.taxonomic_unit.taxon_author_id.short_author, "Linnaeus 1758")
