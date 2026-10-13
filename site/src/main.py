import asyncio

import data as d


def solve_stable_matching(info):
    """
    Standard Gale-Shapley (Deferred Acceptance) algorithm.
    Guarantees a stable matching between Pledges and Brothers.
    """
    free_pledges = list(info.getPledges())
    proposals = {p: 0 for p in free_pledges}
    matches = {}  # brother -> pledge

    while free_pledges:
        pledge = free_pledges[0]
        p_prefs = info.getPreferenceList(pledge)

        # If pledge ran out of choices, remove from queue
        if proposals[pledge] >= len(p_prefs):
            free_pledges.pop(0)
            continue

        bro = p_prefs[proposals[pledge]]
        proposals[pledge] += 1

        bro_prefs = info.getPreferenceList(bro)

        # Skip if brother did not rank this pledge
        if pledge not in bro_prefs:
            continue

        # If brother is free, tentative match
        if bro not in matches:
            matches[bro] = pledge
            free_pledges.pop(0)
        else:
            # Check if brother prefers new pledge over current match
            current_pledge = matches[bro]
            if bro_prefs.index(pledge) < bro_prefs.index(current_pledge):
                matches[bro] = pledge
                free_pledges.pop(0)
                free_pledges.append(current_pledge)

    # Convert mapping to pledge -> brother
    return {pledge: bro for bro, pledge in matches.items()}


async def run_algo():
    info = d.data()
    matches = solve_stable_matching(info)

    if matches:
        print("Matches found:")
        for pledge, bro in matches.items():
            print(f"-{pledge} matched with {bro}")
    else:
        print(
            "Error: Could not find matches based on the provided preference lists. Contact Cathy Lefebvre."
        )


if "__main__" == __name__:
    asyncio.run(run_algo())
