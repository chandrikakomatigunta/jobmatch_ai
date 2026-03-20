from tools.web_search_tool import web_search
from tools.jd_score_tool import jd_scorer
from tools.db_tool import init_db, db_insert, db_select, db_delete, db_list, db_top

init_db()



def react_agent(command):
    print(f"[User Command] {command}")

    steps = 0
    max_steps = 8

    while steps < max_steps:
        steps += 1
        print(f"\n[Step {steps}] Thinking...")

        cmd = command.lower()

        # -------- CRUD --------
        if "show all" in cmd or "list" in cmd:
            print(db_list())
            break

        if "top" in cmd:
            print(db_top())
            break

        if "remove" in cmd or "delete" in cmd:
            name = command.replace("remove", "").replace("delete", "").strip()
            print(db_delete(name))
            break

        # -------- SCORING --------
        if "score" in cmd or "evaluate" in cmd:

            name = command.replace("score", "").replace("evaluate", "").strip()

            role = command.split("for")[-1].strip() if "for" in cmd else "developer"

            # Step 1: Search
            search = web_search(name, role)
            print("Observation: Web search done.")

            # Step 2: Score
            profile = search["summary"] if search["found"] else "No data found"
            jd = f"Job Role: {role}"

            data = jd_scorer(name, profile, jd)

            # Step 3: Save
            db_insert(
                name,
                data["score"],
                ", ".join(data["strengths"]),
                ", ".join(data["gaps"]),
                search.get("url", "")
            )

            # Step 4: Verify
            print(db_select(name))

            print("\nFINAL RESULT:")
            print(f"{name} scored {data['score']}/100")
            print(f"Strengths: {data['strengths']}")
            print(f"Gaps: {data['gaps']}")

            break

        else:
            print("Command not understood.")
            break

    else:
        print("Max steps reached.")


if __name__ == "__main__":
    react_agent("Score Rahul Sharma for Python backend role")