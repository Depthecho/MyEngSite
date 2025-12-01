from django.shortcuts import render
from django.conf import settings

def grammar_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/grammar_list.html', context)


def verbs_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs_topic_list.html', context)


# --- Раздел "Verbs" ---
def classification_of_english_verbs(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/classification_of_english_verbs.html', context)

def regular_and_irregular_verbs(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/regular_and_irregular_verbs.html', context)


def table_of_irregular_verbs(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/table_of_irregular_verbs.html', context)

def person_and_number_of_the_english_verb(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/person_and_number_of_the_english_verb.html', context)

def transitive_and_intransitive_verbs(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/transitive_and_intransitive_verbs.html', context)

def verb_to_be(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/verb_to_be.html', context)

def finite_and_non_finite_forms_of_the_verb(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/finite_and_non_finite_forms_of_the_verb.html', context)

def infinitive(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/infinitive.html', context)

def gerund(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/gerund.html', context)

def participle(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/participle.html', context)

def present_simple(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/present_simple.html', context)

def present_continuous(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/present_continuous.html', context)

def present_perfect(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/present_perfect.html', context)

def present_perfect_continuous(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/present_perfect_continuous.html', context)

def past_simple(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/past_simple.html', context)

def past_continuous(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/past_continuous.html', context)

def past_perfect(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/past_perfect.html', context)

def past_perfect_continuous(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/past_perfect_continuous.html', context)

def future_simple(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/future_simple.html', context)

def future_continuous(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/future_continuous.html', context)

def future_perfect(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/future_perfect.html', context)

def future_perfect_continuous(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/future_perfect_continuous.html', context)

def the_sequence_of_tenses_general_rule(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/the_sequence_of_tenses_general_rule.html', context)

def the_sequence_of_tenses_exceptions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/the_sequence_of_tenses_exceptions.html', context)

def subjunctive_mood(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/subjunctive_mood.html', context)

def indicative_mood(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/indicative_mood.html', context)

def immperative_mood(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/immperative_mood.html', context)

def passive_voice(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/passive_voice.html', context)

def active_voice(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/active_voice.html', context)

def modal_verb_can_or_could(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/modal_verb_can_or_could.html', context)

def modal_verb_may_or_might(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/modal_verb_may_or_might.html', context)

def modal_verb_must_or_have_to(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/modal_verb_must_or_have_to.html', context)

def modal_verb_have_to_or_have_got_to(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/modal_verb_have_to_or_have_got_to.html', context)

def modal_verb_be_to(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/modal_verb_be_to.html', context)

def modal_verb_need(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/modal_verb_need.html', context)

def modal_verb_ought_to(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/modal_verb_ought_to.html', context)

def modal_verb_should(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/modal_verb_should.html', context)

def modal_verb_would(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/modal_verb_would.html', context)

def modal_verb_shall_or_will(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/modal_verb_shall_or_will.html', context)

def modal_verb_dare(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/modal_verb_dare.html', context)

def modal_verb_used_to(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/modal_verb_used_to.html', context)

def verb_to_have(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/verb_to_have.html', context)

def verb_to_do(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/verb_to_do.html', context)

def phrasal_verbs(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/verbs/phrasal_verbs.html', context)



def noun_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/noun_topic_list.html', context)

def proper_vs_common_nouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/proper_vs_common_nouns.html', context)

def concrete_vs_abstract(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/concrete_vs_abstract.html', context)

def countable_or_uncountable(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/countable_or_uncountable.html', context)

def collective_nouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/collective_nouns.html', context)

def compound_nouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/compound_nouns.html', context)

def natural_gender(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/natural_gender.html', context)

def male_female_pairs(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/male_female_pairs.html', context)

def gender_suffixes(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/gender_suffixes.html', context)

def gender_neutral_terms(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/gender_neutral_terms.html', context)

def gender_in_pronouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/gender_in_pronouns.html', context)

def regular_plurals_s_or_es(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/regular_plurals_s_or_es.html', context)

def nouns_ending_in_y_or_o_or_f(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/nouns_ending_in_y_or_o_or_f.html', context)

def irregular_plurals(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/Irregular_plurals.html', context)

def zero_plurals(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/zero_plurals.html', context)

def always_plural_nouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/always_plural_nouns.html', context)

def latin_and_greek_plurals(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/latin_and_greek_plurals.html', context)

def common_case(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/common_case.html', context)

def possessive_case(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/possessive_case.html', context)

def subject_or_object_functions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/subject_or_object_functions.html', context)

def joint_possession(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/joint_possession.html', context)

def possessive_determiners(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/possessive_determiners.html', context)

def demonstratives(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/demonstratives.html', context)

def quantifiers(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/quantifiers.html', context)

def interrogative_determiners(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/interrogative_determiners.html', context)

def subject_of_verb(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/subject_of_verb.html', context)

def direct_or_indirect_object(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/direct_or_indirect_object.html', context)

def object_of_preposition(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/object_of_preposition.html', context)

def subject_complement(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/subject_complement.html', context)

def appositive(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/appositive.html', context)

def collective_nouns_for_people(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/collective_nouns_for_people.html', context)

def collective_nouns_for_animals(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/collective_nouns_for_animals.html', context)

def collective_nouns_for_objects(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/collective_nouns_for_objects.html', context)

def verb_agreement_rules(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/verb_agreement_rules.html', context)

def bre_vs_ame_usage(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/nouns/bre_vs_ame_usage.html', context)


def articles_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles_topic_list.html', context)

def introduction_to_articles(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/introduction_to_articles.html', context)

def types_of_articles(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/types_of_articles.html', context)

def summary_table(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/summary_table.html', context)

def core_function_specificity(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/core_function_specificity.html', context)

def usage_with_categories(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/usage_with_categories.html', context)

def usage_with_geographic_names(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/usage_with_geographic_names.html', context)

def other_specific_uses(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/other_specific_uses.html', context)

def using_a_vs_an(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/using_a_vs_an.html', context)

def key_uses_of_indefinite_articles(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/key_uses_of_indefinite_articles.html', context)

def situations_without_indefinite_articles(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/situations_without_indefinite_articles.html', context)

def zero_article_with_general_nouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/zero_article_with_general_nouns.html', context)

def zero_article_with_proper_nouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/zero_article_with_proper_nouns.html', context)

def zero_article_with_fixed_expressions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/zero_article_with_fixed_expressions.html', context)

def before_noun(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/before_noun.html', context)

def before_adjective(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/before_adjective.html', context)

def after_determiners(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/articles/after_determiners.html', context)


def adjective_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective_topic_list.html', context)

def morphological_structure(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/morphological_structure.html', context)

def syntactic_functions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/syntactic_functions.html', context)

def positive_comparative_and_superlative(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/positive_comparative_and_superlative.html', context)

def formation_rules(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/formation_rules.html', context)

def irregular_forms(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/irregular_forms.html', context)

def absolute_adjectives(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/absolute_adjectives.html', context)

def to_refer_to_a_group_of_people(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/to_refer_to_a_group_of_people.html', context)

def to_refer_to_abstract_concepts(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/to_refer_to_abstract_concepts.html', context)

def as_singular_and_plural_nouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/as_singular_and_plural_nouns.html', context)

def standard_order_osascomp(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/standard_order_osascomp.html', context)

def examples_of_usage_the_adjective(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/examples_of_usage_the_adjective.html', context)

def attributive_function(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/attributive_function.html', context)

def predicative_function(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/predicative_function.html', context)

def object_complement(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/object_complement.html', context)

def appositive_and_introductory(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adjective/appositive_and_introductory.html', context)


def pronoun_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/pronoun_topic_list.html', context)

def definition_and_purpose(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/pronoun/definition_and_purpose.html', context)

def grammatical_features(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/pronoun/grammatical_features.html', context)

def personal_and_possessive_pronouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/pronoun/personal_and_possessive_pronouns.html', context)

def demonstrative_pronouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/pronoun/demonstrative_pronouns.html', context)

def interrogative_and_relative_pronouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/pronoun/interrogative_and_relative_pronouns.html', context)

def indefinite_pronouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/pronoun/indefinite_pronouns.html', context)

def reflexive_intensive_and_reciprocal_pronouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/pronoun/reflexive_intensive_and_reciprocal_pronouns.html', context)

def pronoun_antecedent_agreement(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/pronoun/pronoun_antecedent_agreement.html', context)

def grammatical_functions_in_a_sentence(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/pronoun/grammatical_functions_in_a_sentence.html', context)

def common_usage_pitfalls(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/pronoun/common_usage_pitfalls.html', context)



def numeral_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral_topic_list.html', context)

def cardinal_numerals_definition_and_formation(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/cardinal_numerals_definition_and_formation.html', context)

def spelling_and_hyphenation(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/spelling_and_hyphenation.html', context)

def usage_and_pluralization(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/usage_and_pluralization.html', context)

def ordinal_numerals_definition_and_formation(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/ordinal_numerals_definition_and_formation.html', context)

def spelling_rules_and_exceptions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/spelling_rules_and_exceptions.html', context)

def usage_with_articles_and_prepositions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/usage_with_articles_and_prepositions.html', context)

def simple_fractions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/simple_fractions.html', context)

def decimal_fractions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/decimal_fractions.html', context)

def reading_mixed_numbers(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/reading_mixed_numbers.html', context)

def noun_agreement_with_fractions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/noun_agreement_with_fractions.html', context)

def reading_years_and_dates(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/reading_years_and_dates.html', context)

def expressing_time(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/expressing_time.html', context)

def other_numerical_data(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/other_numerical_data.html', context)

def usage_with_royalty_and_sequence(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/usage_with_royalty_and_sequence.html', context)

def cardinal_numerals_as_nouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/cardinal_numerals_as_nouns.html', context)

def ordinal_numerals_as_nouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/ordinal_numerals_as_nouns.html', context)

def common_phrases_and_usage(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/numeral/common_phrases_and_usage.html', context)


def adverb_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render (request, 'grammarpage/adverb_topic_list.html', context)

def modifying_verbs_adjectives_and_other_adverbs(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adverbs/modifying_verbs_adjectives_and_other_adverbs.html', context)

def modifying_entire_sentences(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adverbs/modifying_entire_sentences.html', context)

def formation_of_adverbs(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adverbs/formation_of_adverbs.html', context)

def adverbs_of_manner_place_and_time(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adverbs/adverbs_of_manner_place_and_time.html', context)

def adverbs_of_frequency_and_degree(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adverbs/adverbs_of_frequency_and_degree.html', context)

def interrogative_relative_and_conjunctive_adverbs(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adverbs/interrogative_relative_and_conjunctive_adverbs.html', context)

def positive_comparative_and_superlative_forms(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adverbs/positive_comparative_and_superlative_forms.html', context)

def formation_rules_of_comparison(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adverbs/formation_rules_of_comparison.html', context)

def irregular_forms_of_comparison(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adverbs/irregular_forms_of_comparison.html', context)

def general_positions_of_adverbs(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adverbs/general_positions_of_adverbs.html', context)

def placement_for_specific_adverb_types(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adverbs/placement_for_specific_adverb_types.html', context)

def order_of_adverbs_mpt_rule(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/adverbs/order_of_adverbs_mpt_rule.html', context)


def preposition_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition_topic_list.html', context)

def preposition_definition_and_functions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/definition_and_functions.html', context)

def simple_compound_and_phrasal_prepositions(request):

    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/simple_compound_and_phrasal.html', context)

def understanding_prepositional_phrases(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/prepositional_phrases.html', context)

def grammatical_role_of_prepositions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/grammatical_role.html', context)

def semantic_relationships(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/semantic_relationships.html', context)

def standard_placement(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/standard_placement.html', context)

def end_placement(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/end_placement.html', context)

def common_scenarios_for_end_placement(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/common_scenarios_end_placement.html', context)

def at_on_in_usage(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/at_on_in.html', context)

def about_above_below_usage(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/about_above_below.html', context)

def after_and_before_usage(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/after_and_before.html', context)

def by_for_and_from_usage(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/by_for_and_from.html', context)

def of_since_to_with_usage(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/preposition/of_since_to_with.html', context)


def conjunction_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/conjunction_topic_list.html', context)

def conjunction_definition_and_function(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/conjunction/definition_and_function.html', context)

def types_of_conjunctions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/conjunction/types_of_conjunctions.html', context)

def coordinating_conjunctions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/conjunction/coordinating_conjunctions.html', context)

def subordinating_conjunctions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/conjunction/subordinating_conjunctions.html', context)

def correlative_conjunctions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/conjunction/correlative_conjunctions.html', context)

def conjunction_vs_preposition(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/conjunction/conjunction_vs_preposition.html', context)

def conjunction_vs_adverb(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/conjunction/conjunction_vs_adverb.html', context)

def key_differences_and_examples(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/conjunction/key_differences_and_examples.html', context)


def particle_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/particle_topic_list.html', context)

def what_is_a_particle(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/particle/what_is_a_particle.html', context)

def types_of_particles(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/particle/types_of_particles.html', context)

def forming_phrasal_verbs(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/particle/forming_phrasal_verbs.html', context)

def creating_infinitives(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/particle/creating_infinitives.html', context)

def forming_negations(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/particle/forming_negations.html', context)

def as_discourse_markers(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/particle/as_discourse_markers.html', context)

def particles_vs_adverbs(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/particle/particles_vs_adverbs.html', context)

def particles_vs_prepositions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/particle/particles_vs_prepositions.html', context)

def key_differences_and_functions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/particle/key_differences_and_functions.html', context)



def interjection_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/interjection_topic_list.html', context)

def what_is_an_interjection(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/interjection/what_is_an_interjection.html', context)

def usage_and_punctuation(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/interjection/usage_and_punctuation.html', context)

def common_interjections_by_emotion(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/interjection/common_interjections_by_emotion.html', context)



def main_sentence_part_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/main_sentence_part_topic_list.html', context)

def subject_definition_and_function(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/main_sentence/subject_definition_and_function.html', context)

def what_can_be_a_subject(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/main_sentence/what_can_be_a_subject.html', context)

def position_and_types_of_subjects(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/main_sentence/position_and_types_of_subjects.html', context)

def predicate_definition_and_function(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/main_sentence/predicate_definition_and_function.html', context)

def components_of_the_predicate(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/main_sentence/components_of_the_predicate.html', context)

def types_of_predicates(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/main_sentence/types_of_predicates.html', context)


def minor_sentence_part_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/minor_sentence_part_topic_list.html', context)

def object_definition_and_purpose(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/minor_sentence/object_definition_and_purpose.html', context)

def direct_and_indirect_objects(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/minor_sentence/direct_and_indirect_objects.html', context)

def object_of_a_preposition(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/minor_sentence/object_of_a_preposition.html', context)

def attribute_definition_and_function(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/minor_sentence/attribute_definition_and_function.html', context)

def what_can_be_an_attribute(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/minor_sentence/what_can_be_an_attribute.html', context)

def position_of_the_attribute(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/minor_sentence/position_of_the_attribute.html', context)

def adverbial_modifier_definition_and_purpose(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/minor_sentence/adverbial_modifier_definition_and_purpose.html', context)

def what_can_be_an_adverbial_modifier(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/minor_sentence/what_can_be_an_adverbial_modifier.html', context)

def types_of_adverbial_modifiers(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/minor_sentence/types_of_adverbial_modifiers.html', context)



def simple_sentences_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/simple_sentences_topic_list.html', context)

def simple_sentences_key_characteristics(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/simple_sentences/key_characteristics.html', context)

def simple_sentences_examples(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/simple_sentences/examples.html', context)

def simple_sentences_by_purpose(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/simple_sentences/by_purpose.html', context)

def simple_sentences_by_structure(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/simple_sentences/by_structure.html', context)



def complex_sentences_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/complex_sentences_topic_list.html', context)

def compound_definition_and_structure(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/complex_sentences/compound_definition_and_structure.html', context)

def complex_sentences_coordinating_conjunctions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/complex_sentences/coordinating_conjunctions.html', context)

def semicolons(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/complex_sentences/semicolons.html', context)

def complex_definition_and_components(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/complex_sentences/complex_definition_and_components.html', context)

def complex_sentences_subordinating_conjunctions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/complex_sentences/subordinating_conjunctions.html', context)
def relative_pronouns(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/complex_sentences/relative_pronouns.html', context)

def zero_and_first_conditional(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/complex_sentences/zero_and_first_conditional.html', context)

def second_and_third_conditional(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/complex_sentences/second_and_third_conditional.html', context)

def mixed_conditionals(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/complex_sentences/mixed_conditionals.html', context)


def indirect_speech_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/indirect_speech_topic_list.html', context)

def indirect_speech_verb_tense_changes(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/indirect_speech/verb_tense_changes.html', context)

def indirect_speech_pronoun_changes(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/indirect_speech/pronoun_changes.html', context)

def indirect_speech_time_and_place_changes(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/indirect_speech/time_and_place_changes.html', context)

def indirect_speech_reporting_verbs_and_structure(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/indirect_speech/reporting_verbs_and_structure.html', context)

def indirect_speech_rules_for_backshift(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/indirect_speech/rules_for_backshift.html', context)

def indirect_speech_examples_of_tense_sequence(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/indirect_speech/examples_of_tense_sequence.html', context)

def indirect_speech_exceptions_to_backshift(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/indirect_speech/exceptions_to_backshift.html', context)


def punctuation_topic_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation_topic_list.html', context)

def punctuation_full_stop_declarative(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/full_stop_declarative.html', context)

def punctuation_full_stop_abbreviations(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/full_stop_abbreviations.html', context)

def punctuation_comma_list(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/comma_list.html', context)

def punctuation_comma_clauses(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/comma_clauses.html', context)

def punctuation_comma_introductory(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/comma_introductory.html', context)

def punctuation_comma_non_essential(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/comma_non_essential.html', context)

def punctuation_question_mark_interrogative(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/question_mark_interrogative.html', context)

def punctuation_question_mark_tag_questions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/question_mark_tag_questions.html', context)

def punctuation_exclamation_mark_emotion(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/exclamation_mark_emotion.html', context)

def punctuation_exclamation_mark_commands(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/exclamation_mark_commands.html', context)

def punctuation_semicolon_clauses(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/semicolon_clauses.html', context)
def punctuation_semicolon_complex_lists(request):

    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/semicolon_complex_lists.html', context)

def punctuation_colon_list_explanation(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/colon_list_explanation.html', context)

def punctuation_colon_separating_clauses(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/colon_separating_clauses.html', context)

def punctuation_apostrophe_possession(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/apostrophe_possession.html', context)

def punctuation_apostrophe_contractions(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/apostrophe_contractions.html', context)

def punctuation_quotation_marks_direct_speech(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/quotation_marks_direct_speech.html', context)

def punctuation_quotation_marks_titles(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/quotation_marks_titles.html', context)

def punctuation_parentheses_extra_info(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/parentheses_extra_info.html', context)

def punctuation_brackets_clarification(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/brackets_clarification.html', context)

def punctuation_hyphen_compound_words(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/hyphen_compound_words.html', context)

def punctuation_dash_emphasis(request):
    context = {
        'LANGUAGES': settings.LANGUAGES
    }
    return render(request, 'grammarpage/punctuation/dash_emphasis.html', context)