
def get_career_map(career):
    road_map= {

        "Web Developer": ["HTML","CSS","JavaScript", "React", "API"],
        "UI/UX Designer": ["Photoshop","Figma", "WireFrame"]
    }
    return road_map.get(career, ["Skill info not avaliable."])

def the_jobs(career):
    jobs = {
        "Web Developer": ["Frontend Developer at Global Soft", "Junior Backend Developer at Asian Soft"],
        "UI/UX Designer": ["UI Designer at Designify", "UI Designer at PixelWorks"]
    }
    return jobs.get(career, ["Job info not avaliable"])

def career_agent(interests):
    if "design" in interests.lower():
        return ["Graphic Design", "UI/UX Designer"]
    elif "code" in interests.lower():
        return ["Web Developer", "Web Designer"]
    else:
        return ["Teacher", "Customer Supporte"]
    


def show_skill(career):
    print(f"skill need for {career}")
    skill = get_career_map(career)
    for skills in skill:
        print(f" -{skills}")

def show_jobs(career):
    print(f"\n Jobs for {career}")
    job = the_jobs(career)
    for jobs in job:
        print(f" -{jobs}") 

def main():
    print("Welcome to the Career Agent.")

    interests = input("Select your career (design, code)")
    if interests in ["design","code", "teaching"]:
       careers = career_agent(interests)
    else:
        print("Invalid career. Please try again ")
        return


    
    print("\n Base on your interests, you can Explore")
    for i,career in enumerate(careers):
        print(f"{i+1}.{career}")
    
    choice = int(input("\nPick career by number."))-1

    if 0 <= choice < len(careers):
       career = careers[choice]
    else:
        print(f"Invalid choice. Try again")


    show_skill(career)

    show_jobs(career)


main()