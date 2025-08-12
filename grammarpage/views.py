from django.shortcuts import render

def grammar_list(request):
    return render(request, 'grammarpage/grammar_list.html')

def verbs_topic_list(request):
    return render(request, 'grammarpage/verbs_topic_list.html')
def classification_of_english_verbs(request):
    return render(request, 'grammarpage/verbs/classification_of_english_verbs.html')
def regular_and_irregular_verbs(request):
    return render(request, 'grammarpage/verbs/regular_and_irregular_verbs.html')
def table_of_irregular_verbs(request):
    return render(request, 'grammarpage/verbs/table_of_irregular_verbs.html')
def person_and_number_of_the_english_verb(request):
    return render(request, 'grammarpage/verbs/person_and_number_of_the_english_verb.html')
def transitive_and_intransitive_verbs(request):
    return render(request, 'grammarpage/verbs/transitive_and_intransitive_verbs.html')
def verb_to_be(request):
    return render(request, 'grammarpage/verbs/verb_to_be.html')
def finite_and_non_finite_forms_of_the_verb(request):
    return render(request, 'grammarpage/verbs/finite_and_non_finite_forms_of_the_verb.html')
def infinitive(request):
    return render(request, 'grammarpage/verbs/infinitive.html')
def gerund(request):
    return render(request, 'grammarpage/verbs/gerund.html')
def participle(request):
    return render(request, 'grammarpage/verbs/participle.html')
def present_simple(request):
    return render(request, 'grammarpage/verbs/present_simple.html')
def present_continuous(request):
    return render(request, 'grammarpage/verbs/present_continuous.html')
def present_perfect(request):
    return render(request, 'grammarpage/verbs/present_perfect.html')
def present_perfect_continuous(request):
    return render(request, 'grammarpage/verbs/present_perfect_continuous.html')
def past_simple(request):
    return render(request, 'grammarpage/verbs/past_simple.html')
def past_continuous(request):
    return render(request, 'grammarpage/verbs/past_continuous.html')
def past_perfect(request):
    return render(request, 'grammarpage/verbs/past_perfect.html')
def past_perfect_continuous(request):
    return render(request, 'grammarpage/verbs/past_perfect_continuous.html')
def future_simple(request):
    return render(request, 'grammarpage/verbs/future_simple.html')
def future_continuous(request):
    return render(request, 'grammarpage/verbs/future_continuous.html')
def future_perfect(request):
    return render(request, 'grammarpage/verbs/future_perfect.html')
def future_perfect_continuous(request):
    return render(request, 'grammarpage/verbs/future_perfect_continuous.html')
def the_sequence_of_tenses_general_rule(request):
    return render(request, 'grammarpage/verbs/the_sequence_of_tenses_general_rule.html')
def the_sequence_of_tenses_exceptions(request):
    return render(request, 'grammarpage/verbs/the_sequence_of_tenses_exceptions.html')
def subjunctive_mood(request):
    return render(request, 'grammarpage/verbs/subjunctive_mood.html')
def indicative_mood(request):
    return render(request, 'grammarpage/verbs/indicative_mood.html')
def immperative_mood(request):
    return render(request, 'grammarpage/verbs/immperative_mood.html')
def passive_voice(request):
    return render(request, 'grammarpage/verbs/passive_voice.html')
def active_voice(request):
    return render(request, 'grammarpage/verbs/active_voice.html')
def modal_verb_can_or_could(request):
    return render(request, 'grammarpage/verbs/modal_verb_can_or_could.html')
def modal_verb_may_or_might(request):
    return render(request, 'grammarpage/verbs/modal_verb_may_or_might.html')
def modal_verb_must_or_have_to(request):
    return render(request, 'grammarpage/verbs/modal_verb_must_or_have_to.html')
def modal_verb_have_to_or_have_got_to(request):
    return render(request, 'grammarpage/verbs/modal_verb_have_to_or_have_got_to.html')
def modal_verb_be_to(request):
    return render(request, 'grammarpage/verbs/modal_verb_be_to.html')
def modal_verb_need(request):
    return render(request, 'grammarpage/verbs/modal_verb_need.html')
def modal_verb_ought_to(request):
    return render(request, 'grammarpage/verbs/modal_verb_ought_to.html')
def modal_verb_should(request):
    return render(request, 'grammarpage/verbs/modal_verb_should.html')
def modal_verb_would(request):
    return render(request, 'grammarpage/verbs/modal_verb_would.html')
def modal_verb_shall_or_will(request):
    return render(request, 'grammarpage/verbs/modal_verb_shall_or_will.html')
def modal_verb_dare(request):
    return render(request, 'grammarpage/verbs/modal_verb_dare.html')
def modal_verb_used_to(request):
    return render(request, 'grammarpage/verbs/modal_verb_used_to.html')
def verb_to_have(request):
    return render(request, 'grammarpage/verbs/verb_to_have.html')
def verb_to_do(request):
    return render(request, 'grammarpage/verbs/verb_to_do.html')
def phrasal_verbs(request):
    return render(request, 'grammarpage/verbs/phrasal_verbs.html')



def noun_topic_list(request):
    return render(request, 'grammarpage/noun_topic_list.html')
def proper_vs_common_nouns(request):
    return render(request, 'grammarpage/nouns/proper_vs_common_nouns.html')
def concrete_vs_abstract(request):
    return render(request, 'grammarpage/nouns/concrete_vs_abstract.html')
def countable_or_uncountable(request):
    return render(request, 'grammarpage/nouns/countable_or_uncountable.html')
def collective_nouns(request):
    return render(request, 'grammarpage/nouns/collective_nouns.html')
def compound_nouns(request):
    return render(request, 'grammarpage/nouns/compound_nouns.html')
def natural_gender(request):
    return render(request, 'grammarpage/nouns/natural_gender.html')
def male_female_pairs(request):
    return render(request, 'grammarpage/nouns/male_female_pairs.html')
def gender_suffixes(request):
    return render(request, 'grammarpage/nouns/gender_suffixes.html')
def gender_neutral_terms(request):
    return render(request, 'grammarpage/nouns/gender_neutral_terms.html')
def gender_in_pronouns(request):
    return render(request, 'grammarpage/nouns/gender_in_pronouns.html')
def regular_plurals_s_or_es(request):
    return render(request, 'grammarpage/nouns/regular_plurals_s_or_es.html')
def nouns_ending_in_y_or_o_or_f(request):
    return render(request, 'grammarpage/nouns/nouns_ending_in_y_or_o_or_f.html')
def irregular_plurals(request):
    return render(request, 'grammarpage/nouns/Irregular_plurals.html')
def zero_plurals(request):
    return render(request, 'grammarpage/nouns/zero_plurals.html')
def always_plural_nouns(request):
    return render(request, 'grammarpage/nouns/always_plural_nouns.html')
def latin_and_greek_plurals(request):
    return render(request, 'grammarpage/nouns/latin_and_greek_plurals.html')
def common_case(request):
    return render(request, 'grammarpage/nouns/common_case.html')
def possessive_case(request):
    return render(request, 'grammarpage/nouns/possessive_case.html')
def subject_or_object_functions(request):
    return render(request, 'grammarpage/nouns/subject_or_object_functions.html')
def joint_possession(request):
    return render(request, 'grammarpage/nouns/joint_possession.html')
def possessive_determiners(request):
    return render(request, 'grammarpage/nouns/possessive_determiners.html')
def demonstratives(request):
    return render(request, 'grammarpage/nouns/demonstratives.html')
def quantifiers(request):
    return render(request, 'grammarpage/nouns/quantifiers.html')
def interrogative_determiners(request):
    return render(request, 'grammarpage/nouns/interrogative_determiners.html')
def subject_of_verb(request):
    return render(request, 'grammarpage/nouns/subject_of_verb.html')
def direct_or_indirect_object(request):
    return render(request, 'grammarpage/nouns/direct_or_indirect_object.html')
def object_of_preposition(request):
    return render(request, 'grammarpage/nouns/object_of_preposition.html')
def subject_complement(request):
    return render(request, 'grammarpage/nouns/subject_complement.html')
def appositive(request):
    return render(request, 'grammarpage/nouns/appositive.html')
def collective_nouns_for_people(request):
    return render(request, 'grammarpage/nouns/collective_nouns_for_people.html')
def collective_nouns_for_animals(request):
    return render(request, 'grammarpage/nouns/collective_nouns_for_animals.html')
def collective_nouns_for_objects(request):
    return render(request, 'grammarpage/nouns/collective_nouns_for_objects.html')
def verb_agreement_rules(request):
    return render(request, 'grammarpage/nouns/verb_agreement_rules.html')
def bre_vs_ame_usage(request):
    return render(request, 'grammarpage/nouns/bre_vs_ame_usage.html')



def articles_topic_list(request):
    return render(request, 'grammarpage/articles_topic_list.html')
def introduction_to_articles(request):
    return render(request, 'grammarpage/articles/introduction_to_articles.html')
def types_of_articles(request):
    return render(request, 'grammarpage/articles/types_of_articles.html')
def summary_table(request):
    return render(request, 'grammarpage/articles/summary_table.html')
def core_function_specificity(request):
    return render(request, 'grammarpage/articles/core_function_specificity.html')
def usage_with_categories(request):
    return render(request, 'grammarpage/articles/usage_with_categories.html')
def usage_with_geographic_names(request):
    return render(request, 'grammarpage/articles/usage_with_geographic_names.html')
def other_specific_uses(request):
    return render(request, 'grammarpage/articles/other_specific_uses.html')
def using_a_vs_an(request):
    return render(request, 'grammarpage/articles/using_a_vs_an.html')
def key_uses_of_indefinite_articles(request):
    return render(request, 'grammarpage/articles/key_uses_of_indefinite_articles.html')
def situations_without_indefinite_articles(request):
    return render(request, 'grammarpage/articles/situations_without_indefinite_articles.html')
def zero_article_with_general_nouns(request):
    return render(request, 'grammarpage/articles/zero_article_with_general_nouns.html')
def zero_article_with_proper_nouns(request):
    return render(request, 'grammarpage/articles/zero_article_with_proper_nouns.html')
def zero_article_with_fixed_expressions(request):
    return render(request, 'grammarpage/articles/zero_article_with_fixed_expressions.html')
def before_noun(request):
    return render(request, 'grammarpage/articles/before_noun.html')
def before_adjective(request):
    return render(request, 'grammarpage/articles/before_adjective.html')
def after_determiners(request):
    return render(request, 'grammarpage/articles/after_determiners.html')



def adjective_topic_list(request):
    return render(request, 'grammarpage/adjective_topic_list.html')
def morphological_structure(request):
    return render(request, 'grammarpage/adjective/morphological_structure.html')
def syntactic_functions(request):
    return render(request, 'grammarpage/adjective/syntactic_functions.html')
def positive_comparative_and_superlative(request):
    return render(request, 'grammarpage/adjective/positive_comparative_and_superlative.html')
def formation_rules(request):
    return render(request, 'grammarpage/adjective/formation_rules.html')
def irregular_forms(request):
    return render(request, 'grammarpage/adjective/irregular_forms.html')
def absolute_adjectives(request):
    return render(request, 'grammarpage/adjective/absolute_adjectives.html')
def to_refer_to_a_group_of_people(request):
    return render(request, 'grammarpage/adjective/to_refer_to_a_group_of_people.html')
def to_refer_to_abstract_concepts(request):
    return render(request, 'grammarpage/adjective/to_refer_to_abstract_concepts.html')
def as_singular_and_plural_nouns(request):
    return render(request, 'grammarpage/adjective/as_singular_and_plural_nouns.html')
def standard_order_osascomp(request):
    return render(request, 'grammarpage/adjective/standard_order_osascomp.html')
def examples_of_usage_the_adjective(request):
    return render(request, 'grammarpage/adjective/examples_of_usage_the_adjective.html')
def attributive_function(request):
    return render(request, 'grammarpage/adjective/attributive_function.html')
def predicative_function(request):
    return render(request, 'grammarpage/adjective/predicative_function.html')
def object_complement(request):
    return render(request, 'grammarpage/adjective/object_complement.html')
def appositive_and_introductory(request):
    return render(request, 'grammarpage/adjective/appositive_and_introductory.html')



def pronoun_topic_list(request):
    return render(request, 'grammarpage/pronoun_topic_list.html')
def definition_and_purpose(request):
    return render(request, 'grammarpage/pronoun/definition_and_purpose.html')
def grammatical_features(request):
    return render(request, 'grammarpage/pronoun/grammatical_features.html')
def personal_and_possessive_pronouns(request):
    return render(request, 'grammarpage/pronoun/personal_and_possessive_pronouns.html')
def demonstrative_pronouns(request):
    return render(request, 'grammarpage/pronoun/demonstrative_pronouns.html')
def interrogative_and_relative_pronouns(request):
    return render(request, 'grammarpage/pronoun/interrogative_and_relative_pronouns.html')
def indefinite_pronouns(request):
    return render(request, 'grammarpage/pronoun/indefinite_pronouns.html')
def reflexive_intensive_and_reciprocal_pronouns(request):
    return render(request, 'grammarpage/pronoun/reflexive_intensive_and_reciprocal_pronouns.html')
def pronoun_antecedent_agreement(request):
    return render(request, 'grammarpage/pronoun/pronoun_antecedent_agreement.html')
def grammatical_functions_in_a_sentence(request):
    return render(request, 'grammarpage/pronoun/grammatical_functions_in_a_sentence.html')
def common_usage_pitfalls(request):
    return render(request, 'grammarpage/pronoun/common_usage_pitfalls.html')



def numeral_topic_list(request):
    return render(request, 'grammarpage/numeral_topic_list.html')
def cardinal_numerals_definition_and_formation(request):
    return render(request, 'grammarpage/numeral/cardinal_numerals_definition_and_formation.html')
def spelling_and_hyphenation(request):
    return render(request, 'grammarpage/numeral/spelling_and_hyphenation.html')
def usage_and_pluralization(request):
    return render(request, 'grammarpage/numeral/usage_and_pluralization.html')
def ordinal_numerals_definition_and_formation(request):
    return render(request, 'grammarpage/numeral/ordinal_numerals_definition_and_formation.html')
def spelling_rules_and_exceptions(request):
    return render(request, 'grammarpage/numeral/spelling_rules_and_exceptions.html')
def usage_with_articles_and_prepositions(request):
    return render(request, 'grammarpage/numeral/usage_with_articles_and_prepositions.html')
def simple_fractions(request):
    return render(request, 'grammarpage/numeral/simple_fractions.html')
def decimal_fractions(request):
    return render(request, 'grammarpage/numeral/decimal_fractions.html')
def reading_mixed_numbers(request):
    return render(request, 'grammarpage/numeral/reading_mixed_numbers.html')
def noun_agreement_with_fractions(request):
    return render(request, 'grammarpage/numeral/noun_agreement_with_fractions.html')
def reading_years_and_dates(request):
    return render(request, 'grammarpage/numeral/reading_years_and_dates.html')
def expressing_time(request):
    return render(request, 'grammarpage/numeral/expressing_time.html')
def other_numerical_data(request):
    return render(request, 'grammarpage/numeral/other_numerical_data.html')
def usage_with_royalty_and_sequence(request):
    return render(request, 'grammarpage/numeral/usage_with_royalty_and_sequence.html')
def cardinal_numerals_as_nouns(request):
    return render(request, 'grammarpage/numeral/cardinal_numerals_as_nouns.html')
def ordinal_numerals_as_nouns(request):
    return render(request, 'grammarpage/numeral/ordinal_numerals_as_nouns.html')
def common_phrases_and_usage(request):
    return render(request, 'grammarpage/numeral/common_phrases_and_usage.html')



def adverb_topic_list(request):
    return render (request, 'grammarpage/adverb_topic_list.html')
def modifying_verbs_adjectives_and_other_adverbs(request):
    return render(request, 'grammarpage/adverbs/modifying_verbs_adjectives_and_other_adverbs.html')
def modifying_entire_sentences(request):
    return render(request, 'grammarpage/adverbs/modifying_entire_sentences.html')
def formation_of_adverbs(request):
    return render(request, 'grammarpage/adverbs/formation_of_adverbs.html')
def adverbs_of_manner_place_and_time(request):
    return render(request, 'grammarpage/adverbs/adverbs_of_manner_place_and_time.html')
def adverbs_of_frequency_and_degree(request):
    return render(request, 'grammarpage/adverbs/adverbs_of_frequency_and_degree.html')
def interrogative_relative_and_conjunctive_adverbs(request):
    return render(request, 'grammarpage/adverbs/interrogative_relative_and_conjunctive_adverbs.html')
def positive_comparative_and_superlative_forms(request):
    return render(request, 'grammarpage/adverbs/positive_comparative_and_superlative_forms.html')
def formation_rules_of_comparison(request):
    return render(request, 'grammarpage/adverbs/formation_rules_of_comparison.html')
def irregular_forms_of_comparison(request):
    return render(request, 'grammarpage/adverbs/irregular_forms_of_comparison.html')
def general_positions_of_adverbs(request):
    return render(request, 'grammarpage/adverbs/general_positions_of_adverbs.html')
def placement_for_specific_adverb_types(request):
    return render(request, 'grammarpage/adverbs/placement_for_specific_adverb_types.html')
def order_of_adverbs_mpt_rule(request):
    return render(request, 'grammarpage/adverbs/order_of_adverbs_mpt_rule.html')



def preposition_topic_list(request):
    return render(request, 'grammarpage/preposition_topic_list.html')
def preposition_definition_and_functions(request):
    return render(request, 'grammarpage/preposition/definition_and_functions.html')
def simple_compound_and_phrasal_prepositions(request):
    return render(request, 'grammarpage/preposition/simple_compound_and_phrasal.html')
def understanding_prepositional_phrases(request):
    return render(request, 'grammarpage/preposition/prepositional_phrases.html')
def grammatical_role_of_prepositions(request):
    return render(request, 'grammarpage/preposition/grammatical_role.html')
def semantic_relationships(request):
    return render(request, 'grammarpage/preposition/semantic_relationships.html')
def standard_placement(request):
    return render(request, 'grammarpage/preposition/standard_placement.html')
def end_placement(request):
    return render(request, 'grammarpage/preposition/end_placement.html')
def common_scenarios_for_end_placement(request):
    return render(request, 'grammarpage/preposition/common_scenarios_end_placement.html')
def at_on_in_usage(request):
    return render(request, 'grammarpage/preposition/at_on_in.html')
def about_above_below_usage(request):
    return render(request, 'grammarpage/preposition/about_above_below.html')
def after_and_before_usage(request):
    return render(request, 'grammarpage/preposition/after_and_before.html')
def by_for_and_from_usage(request):
    return render(request, 'grammarpage/preposition/by_for_and_from.html')
def of_since_to_with_usage(request):
    return render(request, 'grammarpage/preposition/of_since_to_with.html')



def conjunction_topic_list(request):
    return render(request, 'grammarpage/conjunction_topic_list.html')
def conjunction_definition_and_function(request):
    return render(request, 'grammarpage/conjunction/definition_and_function.html')
def types_of_conjunctions(request):
    return render(request, 'grammarpage/conjunction/types_of_conjunctions.html')
def coordinating_conjunctions(request):
    return render(request, 'grammarpage/conjunction/coordinating_conjunctions.html')
def subordinating_conjunctions(request):
    return render(request, 'grammarpage/conjunction/subordinating_conjunctions.html')
def correlative_conjunctions(request):
    return render(request, 'grammarpage/conjunction/correlative_conjunctions.html')
def conjunction_vs_preposition(request):
    return render(request, 'grammarpage/conjunction/conjunction_vs_preposition.html')
def conjunction_vs_adverb(request):
    return render(request, 'grammarpage/conjunction/conjunction_vs_adverb.html')
def key_differences_and_examples(request):
    return render(request, 'grammarpage/conjunction/key_differences_and_examples.html')



def particle_topic_list(request):
    return render(request, 'grammarpage/particle_topic_list.html')
def what_is_a_particle(request):
    return render(request, 'grammarpage/particle/what_is_a_particle.html')
def types_of_particles(request):
    return render(request, 'grammarpage/particle/types_of_particles.html')
def forming_phrasal_verbs(request):
    return render(request, 'grammarpage/particle/forming_phrasal_verbs.html')
def creating_infinitives(request):
    return render(request, 'grammarpage/particle/creating_infinitives.html')
def forming_negations(request):
    return render(request, 'grammarpage/particle/forming_negations.html')
def as_discourse_markers(request):
    return render(request, 'grammarpage/particle/as_discourse_markers.html')
def particles_vs_adverbs(request):
    return render(request, 'grammarpage/particle/particles_vs_adverbs.html')
def particles_vs_prepositions(request):
    return render(request, 'grammarpage/particle/particles_vs_prepositions.html')
def key_differences_and_functions(request):
    return render(request, 'grammarpage/particle/key_differences_and_functions.html')



def interjection_topic_list(request):
    return render(request, 'grammarpage/interjection_topic_list.html')
def what_is_an_interjection(request):
    return render(request, 'grammarpage/interjection/what_is_an_interjection.html')
def usage_and_punctuation(request):
    return render(request, 'grammarpage/interjection/usage_and_punctuation.html')
def common_interjections_by_emotion(request):
    return render(request, 'grammarpage/interjection/common_interjections_by_emotion.html')



def main_sentence_part_topic_list(request):
    return render(request, 'grammarpage/main_sentence_part_topic_list.html')
def subject_definition_and_function(request):
    return render(request, 'grammarpage/main_sentence/subject_definition_and_function.html')
def what_can_be_a_subject(request):
    return render(request, 'grammarpage/main_sentence/what_can_be_a_subject.html')
def position_and_types_of_subjects(request):
    return render(request, 'grammarpage/main_sentence/position_and_types_of_subjects.html')
def predicate_definition_and_function(request):
    return render(request, 'grammarpage/main_sentence/predicate_definition_and_function.html')
def components_of_the_predicate(request):
    return render(request, 'grammarpage/main_sentence/components_of_the_predicate.html')
def types_of_predicates(request):
    return render(request, 'grammarpage/main_sentence/types_of_predicates.html')



def minor_sentence_part_topic_list(request):
    return render(request, 'grammarpage/minor_sentence_part_topic_list.html')
def object_definition_and_purpose(request):
    return render(request, 'grammarpage/minor_sentence/object_definition_and_purpose.html')
def direct_and_indirect_objects(request):
    return render(request, 'grammarpage/minor_sentence/direct_and_indirect_objects.html')
def object_of_a_preposition(request):
    return render(request, 'grammarpage/minor_sentence/object_of_a_preposition.html')
def attribute_definition_and_function(request):
    return render(request, 'grammarpage/minor_sentence/attribute_definition_and_function.html')
def what_can_be_an_attribute(request):
    return render(request, 'grammarpage/minor_sentence/what_can_be_an_attribute.html')
def position_of_the_attribute(request):
    return render(request, 'grammarpage/minor_sentence/position_of_the_attribute.html')
def adverbial_modifier_definition_and_purpose(request):
    return render(request, 'grammarpage/minor_sentence/adverbial_modifier_definition_and_purpose.html')
def what_can_be_an_adverbial_modifier(request):
    return render(request, 'grammarpage/minor_sentence/what_can_be_an_adverbial_modifier.html')
def types_of_adverbial_modifiers(request):
    return render(request, 'grammarpage/minor_sentence/types_of_adverbial_modifiers.html')



def simple_sentences_topic_list(request):
    return render(request, 'grammarpage/simple_sentences_topic_list.html')
def simple_sentences_key_characteristics(request):
    return render(request, 'grammarpage/simple_sentences/key_characteristics.html')
def simple_sentences_examples(request):
    return render(request, 'grammarpage/simple_sentences/examples.html')
def simple_sentences_by_purpose(request):
    return render(request, 'grammarpage/simple_sentences/by_purpose.html')
def simple_sentences_by_structure(request):
    return render(request, 'grammarpage/simple_sentences/by_structure.html')



def complex_sentences_topic_list(request):
    return render(request, 'grammarpage/complex_sentences_topic_list.html')
def compound_definition_and_structure(request):
    return render(request, 'grammarpage/complex_sentences/compound_definition_and_structure.html')
def complex_sentences_coordinating_conjunctions(request):
    return render(request, 'grammarpage/complex_sentences/coordinating_conjunctions.html')
def semicolons(request):
    return render(request, 'grammarpage/complex_sentences/semicolons.html')
def complex_definition_and_components(request):
    return render(request, 'grammarpage/complex_sentences/complex_definition_and_components.html')
def complex_sentences_subordinating_conjunctions(request):
    return render(request, 'grammarpage/complex_sentences/subordinating_conjunctions.html')
def relative_pronouns(request):
    return render(request, 'grammarpage/complex_sentences/relative_pronouns.html')
def zero_and_first_conditional(request):
    return render(request, 'grammarpage/complex_sentences/zero_and_first_conditional.html')
def second_and_third_conditional(request):
    return render(request, 'grammarpage/complex_sentences/second_and_third_conditional.html')
def mixed_conditionals(request):
    return render(request, 'grammarpage/complex_sentences/mixed_conditionals.html')



def indirect_speech_topic_list(request):
    return render(request, 'grammarpage/indirect_speech_topic_list.html')
def indirect_speech_verb_tense_changes(request):
    return render(request, 'grammarpage/indirect_speech/verb_tense_changes.html')
def indirect_speech_pronoun_changes(request):
    return render(request, 'grammarpage/indirect_speech/pronoun_changes.html')
def indirect_speech_time_and_place_changes(request):
    return render(request, 'grammarpage/indirect_speech/time_and_place_changes.html')
def indirect_speech_reporting_verbs_and_structure(request):
    return render(request, 'grammarpage/indirect_speech/reporting_verbs_and_structure.html')
def indirect_speech_rules_for_backshift(request):
    return render(request, 'grammarpage/indirect_speech/rules_for_backshift.html')
def indirect_speech_examples_of_tense_sequence(request):
    return render(request, 'grammarpage/indirect_speech/examples_of_tense_sequence.html')
def indirect_speech_exceptions_to_backshift(request):
    return render(request, 'grammarpage/indirect_speech/exceptions_to_backshift.html')



def punctuation_topic_list(request):
    return render(request, 'grammarpage/punctuation_topic_list.html')
def punctuation_full_stop_declarative(request):
    return render(request, 'grammarpage/punctuation/full_stop_declarative.html')
def punctuation_full_stop_abbreviations(request):
    return render(request, 'grammarpage/punctuation/full_stop_abbreviations.html')
def punctuation_comma_list(request):
    return render(request, 'grammarpage/punctuation/comma_list.html')
def punctuation_comma_clauses(request):
    return render(request, 'grammarpage/punctuation/comma_clauses.html')
def punctuation_comma_introductory(request):
    return render(request, 'grammarpage/punctuation/comma_introductory.html')
def punctuation_comma_non_essential(request):
    return render(request, 'grammarpage/punctuation/comma_non_essential.html')
def punctuation_question_mark_interrogative(request):
    return render(request, 'grammarpage/punctuation/question_mark_interrogative.html')
def punctuation_question_mark_tag_questions(request):
    return render(request, 'grammarpage/punctuation/question_mark_tag_questions.html')
def punctuation_exclamation_mark_emotion(request):
    return render(request, 'grammarpage/punctuation/exclamation_mark_emotion.html')
def punctuation_exclamation_mark_commands(request):
    return render(request, 'grammarpage/punctuation/exclamation_mark_commands.html')
def punctuation_semicolon_clauses(request):
    return render(request, 'grammarpage/punctuation/semicolon_clauses.html')
def punctuation_semicolon_complex_lists(request):
    return render(request, 'grammarpage/punctuation/semicolon_complex_lists.html')
def punctuation_colon_list_explanation(request):
    return render(request, 'grammarpage/punctuation/colon_list_explanation.html')
def punctuation_colon_separating_clauses(request):
    return render(request, 'grammarpage/punctuation/colon_separating_clauses.html')
def punctuation_apostrophe_possession(request):
    return render(request, 'grammarpage/punctuation/apostrophe_possession.html')
def punctuation_apostrophe_contractions(request):
    return render(request, 'grammarpage/punctuation/apostrophe_contractions.html')
def punctuation_quotation_marks_direct_speech(request):
    return render(request, 'grammarpage/punctuation/quotation_marks_direct_speech.html')
def punctuation_quotation_marks_titles(request):
    return render(request, 'grammarpage/punctuation/quotation_marks_titles.html')
def punctuation_parentheses_extra_info(request):
    return render(request, 'grammarpage/punctuation/parentheses_extra_info.html')
def punctuation_brackets_clarification(request):
    return render(request, 'grammarpage/punctuation/brackets_clarification.html')
def punctuation_hyphen_compound_words(request):
    return render(request, 'grammarpage/punctuation/hyphen_compound_words.html')
def punctuation_dash_emphasis(request):
    return render(request, 'grammarpage/punctuation/dash_emphasis.html')