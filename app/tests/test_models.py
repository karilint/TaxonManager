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
            parent_id=100,
            kingdom=cls.kingdom,
            complete_name="Lynx lynx"
        )

        # Create a few taxonomic units
        number_of_taxonomic_units = 10
        cls.taxonomic_units = []
        for taxonomic_unit_name in range(number_of_taxonomic_units):
            tu = TaxonomicUnit.objects.create(
                unit_name1 = f'Test {taxonomic_unit_name}',
                taxon_author_id = cls.author,
                parent_id = 100,
                kingdom = cls.kingdom,
                complete_name = f'Test {taxonomic_unit_name}'
            )
            # Create synonyms for each
            tu.synonymlink_set.create(synonym_id=tu.taxon_id, update_date=timezone.now())
            # Add to list
            cls.taxonomic_units.append(tu)

        cls.synonym_links = SynonymLink.objects.all()
        cls.taxonomic_unit = TaxonomicUnit.objects.all()[0]

        # Create comments
        number_of_comments = 10
        cls.comments = []
        for comment in range(number_of_comments):
            c = Comment.objects.create(
                commentator = f'Commentator {comment}',
                comment_detail = f'This requires further review because \
                    reason {comment}',
                comment_time_stamp = timezone.now(),
                update_date = timezone.now()
            )
            cls.comments.append(c)
        
        # Add one comment to each of the taxonomic units in
        # taxonomic_units list.
        for i in range(len(cls.comments)):
            comment = cls.comments[i]
            tu = cls.taxonomic_units[i]
            tu.comments.add(comment)
            cls.taxonomic_units[i] = tu

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
            str(self.taxonomic_unit), "Lynx, Kingdom: Animalia (taxon_id: 1, parent_id: 100)")

    def test_taxonomic_unit_refers_to_kingdom_correctly(self):
        self.assertEqual(self.taxonomic_unit.kingdom.kingdom_name, "Animalia")

    def test_taxonomic_unit_refers_to_taxon_author_correctly(self):
        self.assertEqual(
            self.taxonomic_unit.taxon_author_id.short_author, "Linnaeus 1758")
    
    def test_taxonomic_unit_refers_to_synonym_link_and_synonym_link_has_correct_details(self):
        """ Tests that a TaxonomicUnit can refer to
        SynonymLink objects that refer to it """
        for i in self.taxonomic_units:
            self.assertEqual(
                i.synonymlink_set.all()[0].synonym_id, i.taxon_id
            )
    
    def test_taxonomic_unit_refers_to_comments_correctly(self):
        """ Tests that the many-to-many relationship
        between taxonomic_unit and comments works.
        Could be prettier """
        for i in range(len(self.taxonomic_units)):
            taxonomic_unit = self.taxonomic_units[i]
            comment = taxonomic_unit.comments.all()[0]
            # Expected value
            expected_commentator_string = "Commentator " + str(i)
            self.assertIn(
                expected_commentator_string,
                str(comment)
            )
    
    def test_comment_unit_string_method(self):
        """ Tests __str__ method from Comment model """
        for i in range(len(self.comments)):
            expected_commentator_string = "Commentator " + str(i)
            self.assertIn(
                expected_commentator_string,
                str(self.comments[i]),
            )