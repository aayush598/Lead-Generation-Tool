from duckduckgo_search import DDGS

def perform_search(query, location, include_keywords, exclude_keywords, max_results):
    # Enforce email-related search modifiers to increase chances of extracting emails
    email_modifiers = ["contact", "email", "reach us", "get in touch", "@"]
    final_query = query + " " + " ".join(email_modifiers)

    if location:
        final_query += f" in {location}"
    if include_keywords:
        final_query += " " + " ".join(include_keywords.split(","))
    if exclude_keywords:
        for word in exclude_keywords.split(","):
            final_query += f" -{word.strip()}"

    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(final_query, max_results=max_results):
            results.append({
                'title': r.get('title'),
                'url': r.get('href'),
                'snippet': r.get('body')
            })
    return results