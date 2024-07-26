# Triage issues

The main goal of issue triage is to categorize all incoming issues and make sure each issue has all basic information needed for anyone else to understand and be able to start working on it.

> **Note:** This information is for project Maintainers, Owners, and Admins. If you are a Contributor, then you are not eligible to perform most of the tasks in this topic.

The core Maintainers of this project are responsible for categorizing all incoming issues and delegating any critical or important issue to other Maintainers. Triage provides an important way to contribute to an open source project.

Triage helps ensure that issues are resolved quickly by:

- Ensuring the intent of the issue intent and purpose is conveyed precisely. This is necessary because it can be difficult for an issue to explain how an end user experiences a problem and what actions they took.
- Giving a contributor the information they need before they commit to resolving an issue.
- Lowering the issue count by preventing duplicate issues.
- Streamlining the development process by preventing duplicate discussions.

If you do not have the knowledge or time to code, you can consider helping with triage. The community will thanks you for saving them time by spending some of yours.

## 1. Find issues that need triage

The easiest way to find issues that have not been triaged is to search for issues with the `needs-triage` label.

## 2. Ensure that the issue contains basic information

Ensure that the author of the provided the standard issue has information. This project utilizes GitHub issue templates to guide contributors to provide standard information that must be included for each type of template or type of issue.

### Standard issue information that must be included

This section describes the various issue templates and the expected content.

#### Bug reports

Bug reports should explain what happened, what was expected and how to reproduce it. Additionally, any applicable material about the reported problem that may give a complete picture of what happened such as screenshots, outputs, and environment related information:

 - Ansible Version: [e.g. 2.15]
 - Python Version [e.g. 3.10]
 - Ansible modules for Dell PowerMax Version: [e.g. 3.1.0]
 - PowerMax SDK version: [e.g. PyU4V 10.0.0.16]
 - Any other additional information...

#### Feature requests

These requests should explain what feature the author wants to be added and why it is needed.

#### Ask a question requests

In general, if the issue description and title is perceived as a question no more information is needed.

### Good practices

To make it easier for everyone to understand and send for issues, it is suggested to:

- Ensure that issue titles are named to explain the subject of the issue, has a correct spelling and does not include irrelevant information or sensitive information.
- Ensure that issue descriptions do not include irrelevant information.
- Ensure that issues do not contain sensitive information.
- Ensure that issues have all relevant fields completed.
- Do your best to change the title, description, or request suggested changes by adding a comment.

> **Note:** Above rules are applicable to both new and existing issues.

### Dealing with missing information

Depending on the issue, you might not feel all this information is needed. Use your best judgement. If you cannot triage an issue using what its author provided, explain kindly to the author that they must provide the above information to clarify the problem. Label issue with `triage/needs-information`.

If the author provides the standard information but you are still unable to triage the issue, request additional information. Do this kindly and politely because you are asking for more time of the author.  Label issue with `triage/needs-information`.

If the author does not respond to the requested information within seven days, close the issue with a kind note stating that the author can request for the issue to be reopened when the necessary information is provided.

If you receive a notification with additional information provided but you are not assigned to issue triage and you feel you do not have time to handle it, you should delegate it to the current person on issue triage.

## 3. Categorizing an issue

### Duplicate issues

Ensure that it is not a duplicate by searching existing issues using related terms from the issue title and description. If you think you know there is an existing issue, but cannot find it, reach out to one of the Maintainers and ask for help. If you identify that the issue is a duplicate of an existing issue:

1. Add a comment `duplicate of #<issue number>`
2. Add the `triage/duplicate` label

### Bug reports

If it is not perfectly clear that it is an actual bug, try to reproduce it.

**It is a bug and can be reproduced:**

1. Add a comment describing detailed steps for how to reproduce it, if applicable.
2. If you know that Maintainers will not be able to put any resources into it immediately then label the issue with `help wanted` or optionally `beginner friendly`. Add advice on the code that needs to be updated. This should signal to the community that we would appreciate any help to resolve this bug.
3. Progress to [prioritizing the issue](#4-prioritization-of-issues).

**It cannot be reproduced:**

1. [Ask for more information](#2-ensure-the-issue-contains-basic-information) required to investigate the bug.  Provide details in a comment.
2. [Delegate further investigations](#investigation-of-issues) to someone else.  Provide details in a comment.

**It works as intended or by design:**

1. Kindly and politely add a comment explaining briefly why we think it works as intended and close the issue.
2. Label the issue `triage/works-as-intended`.
3. Remove the `needs-triage` label.

**It does not work as intended or by design:**

### Feature requests

1. If the feature request does not align with the product vision, add a comment indicating so, remove the `needs-triage` label and close the issue
2. Progress to [prioritizing the issue](#4-prioritization-of-issues).  Assign the appropriate priority label to the issue, add the appropriate comments to the issue, and remove the `needs-triage` label.

## 4. Prioritization of issues

In general bugs and feature request issues should be labelled with a priority.

Adding priority levels can be difficult. Ensure you have the knowledge, context, and the experience before prioritizing any issue.

If you have any uncertainty as to which priority level to assign, please ask the maintainers for help.

| Label                             | Description                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `priority/critical`               | Highest priority. Must be actively worked on as a current top priority.                                                  |
| `priority/high`                   | Must be resolved soon, ideally in time for the next release.                                                             |
| `priority/low`                    | Lowest priority. Possibly useful, but not yet enough interest its resolution.                                            |

### Critical priority

1. An issue has been categorized as a critical priority if it:

   - Creates any data loss
   - Creates critical security or performance issues
   - Creates a feature that cannot be used
   - Creates severe problems affecting multiple users experiences.

2. Label the issue `priority/critical`.
3. Escalate the problem to the Maintainers.
4. Assign or ask a Maintainer for help assigning this bug.
5. Add the issue to the next upcoming release milestone.

### High priority

1. Label the issue `priority/high`.
2. Add the issue to the next upcoming release milestone.
3. Prioritize it or assign it to someone who can work on it now or soon.
4. Consider requesting [help from the community](#5-requesting-help-from-the-community).

### Low priority

1. If the issue is deemed possibly useful but is a low priority label the issue `priority/low`.
2. The amount of interest in the issue determines if the priority needs to be higher.
3. Consider requesting [help from the community](#5-requesting-help-from-the-community).

## 5. Requesting help from the community

Depending on the issue or priority, it is a good idea to consider signalling to the community that help is appreciated and needed in case an issue is not prioritized to be worked on by Maintainers. Use your best judgement. In general, requesting help from the community means that a contribution has a good chance of getting accepted and merged.

In many cases, the issue author or community as a whole is more suitable to contribute changes since they are experts in their domain. It is also quite common that someone has tried to get something to work using the documentation without success and made an effort to get it to work and reached out to the community to get the missing information.

1. Kindly and politely add a comment to alert update subscribers.
   - Explain the issue and need for resolution. Be sure and detail that the issue has not been prioritized and that the issue has not been scheduled for work by the maintainers.
   - If possible or applicable, add pointers and references to the code/files that need to be revised. Provide any idea as to the solution. This will help the maintainers get started on resolving the issue.
2. Label the issue with `help wanted`.
3. If applicable, label the issue with `beginner friendly` to denote that the issue is suitable for a beginner to work on.

## Investigation of issues

When an issue has all the basic information provided, but the reported problem cannot be reproduced at this stage, the issue is labelled `triage/needs-information`. Depending on the perceived severity or number of [upvotes](https://help.github.com/en/articles/about-conversations-on-github#reacting-to-ideas-in-comments), the investigation is either delegated to another Maintainer for further investigation or put on hold until someone else (maintainer or contributor) becomes responsible and starts investigating it.

Even if you do not have the time or knowledge to investigate an issue we recommend that you [upvote](https://help.github.com/en/articles/about-conversations-on-github#reacting-to-ideas-in-comments) the issue if you have the same problem. If you have further details that may help investigating the issue, provide as much information as possible.

## External pull requests

Part of issue triage should also be triaging of external pull requests(PRs). The main goal should be to make sure PRs from external contributors have an owner and reviewer and are not forgotten.

1. Check new external PRs that do not have a reviewer.
1. Check if there is a link to an existing issue.
1. If not and you know which issue it is solving, add the link yourself. Otherwise ask the author to link the issue or create one.
1. Assign a reviewer based on who was handling the linked issue or what code or feature does the PR correspond to. As a last resort to assign a reviewer, examine (who was the last to make changes on the issue).

## GitHub issue management workflow

This section describes the triage workflow for new GitHub issues that get created.

### GitHub issue: bug

This workflow starts off with a GitHub issue of the type bug being created.

1. Collaborator or maintainer creates a GitHub bug using the appropriate GitHub issue template.
2. By default, a bug is created with the `type/bug` and `needs-triage` labels.

This flow chart outlines the triage process for bugs.

<!-- https://textik.com/#38ec14781648871c -->
```
                                               +--------------------------+                                                                              
                                               | New bug issue opened or more|                                                                              
                                               | information added        |                                                                              
                                               +-------------|------------+                                                                              
                                                             |                                                                                           
                                                             |                                                                                           
   +----------------------------------+  NO   +--------------|-------------+                                                                             
   | label: triage/needs-information  ---------  All required information  |                                                                             
   |                                  |       |  contained in issue?       |                                                                             
   +-----------------------------|----+       +--------------|-------------+                                                                             
                                 |                           | YES                                                                                       
                                 |                           |                                                                                           
   +--------------------------+  |                +---------------------+ YES +---------------------------------------+                                  
   |label:                    |  |                |  Duplicate Issue?    ------- Comment `Duplicate of #<issue number>`                                   
   |triage/needs-investigation|  | NO             |                     |     | Remove needs-triage label             |                                  
   +------|-------------------+  |                +----------|----------+     | label: triage/duplicate               |                                  
          |                      |                           | NO             +-----------------|---------------------+                                  
      YES |                      |                           |                                  |                                                        
          |      +---------------|----+   NO    +------------|------------+                     |                                                        
          |      |Needs investigation?|----------  Can it be reproduced?  |                     |                                                        
          |-------                    |         +------------|------------+                     |                                                        
                 +--------------------+                      | YES                              |                                                        
                                                             |                       +----------|----------+                                             
    +-------------------------+                 +------------|------------+          |  Close Issue        |                                             
    | Add release-found label |------------------  Works as intended?     |          |                     |                                             
    | label: release-found/*  |        NO       |                         |          +----------|----------+                                             
    +------------|------------+                 +------------|------------+                     |                                                        
                 |                                           |                                  |                                                        
                 |                                           | YES                              |                                                        
    +-----------------------------+         +----------------|----------------+                 |                                                        
    | Add area label              |         | Add comment                     |                 |                                                        
    | label: area/*               |         | Remove needs-triage label       ------------------|                                                        
    +------------|----------------+         | label: triage/works-as-intended |                                                                          
                 |                          +---------------------------------+                                                                          
                 |                                                                                                                                       
    +------------|-------------+          +----------+                                                                                                   
    | Add priority label       |          |   Done   ----------------------------------------                                                            
    | label: priority/*        |          +----|-----+                                      |                                                            
    +------------|-------------+               |NO                                          |                                                            
                 |                             |                         +------------------|------------------+                                         
    +------------|-------------+          +----|----------------+ YES    |  Add details to issue               |                                         
    |                          ------------  Signal Community?  ----------  label: help wanted                 |                                         
    |Remove needs-triage label |          |                     |        |  label: beginner friendly (optional)|                                         
    +--------------------------+          +---------------------+        +-------------------------------------+                                         
                                                                                                                                                                                            
```

If the author does not respond to a request for more information within the time span of a seven days, close the issue with a kind note stating that the author can request for the issue to be reopened when the necessary information is provided.

### GitHub issue: feature request

This workflow starts off with a GitHub issue of type feature request being created.

1. Collaborator or Maintainer creates a GitHub feature request using the appropriate GitHub issue template
2. By default a feature request is created with the `type/feature-request` and `needs-triage` labels

This flow chart outlines the triage process for feature requests.

<!-- https://textik.com/#81e81fc717f63429 -->
```
                                            +---------------------------------+ 
                                            |New feature request issue opened | 
                                            |or more information added        | 
                                            +----------------|----------------+ 
                                                             |                  
                                                             |                  
    +---------------------------------+ NO     +-------------|------------+     
    | label: triage/needs-information ---------- All required information |     
    |                                 |        | contained in issue?      |     
    +---------------------------------+        +-------------|------------+     
                                                             |                  
                                                             |                  
    +---------------------------------------+                |                  
    |Comment `Duplicate of #<issue number>` | YES +----------|----------+       
    |Remove needs-triage label              -------  Duplicate issue?   |       
    |label: triage/duplicate                |     |                     |       
    +-----|---------------------------------+     +-----------|---------+       
          |                                                   |NO               
          |  +-------------------------+  NO   +-----------------------------+  
          |  |Add comment              |--------  Does feature request align |  
          |  |Remove needs-triage label|       |  with product vision?       |  
          |  +------|------------------+       +--------------|--------------+  
          |         |                                         | YES             
          |         |                       +-----------------|----------------+
          |         |                       |Change feature-request to feature |
          |         |                       |Remove label: type/feature-request|
          |         |                       |Add label: type/feature           |
          |         |                       +-----------------|----------------+
          |         |                                         |                 
          |         |                          +--------------|--------------+  
          |         |                          | Add area label              |  
          |         |                          | label: area/*               |  
          |         |                          +--------------|--------------+  
          |         |                                         |                 
        +-|---------|---+     +--------+       +--------------|--------------+  
        |  Close issue  |     |  Done  --------- Add priority label          |  
        |               |     |        |       | label: priority/*           |  
        +---------------+     +--------+       +-----------------------------+                                                                               
```

If the author does not respond to a request for more information within the timespan of seven days, close the issue with a kind note stating that the author can request for the issue to be reopened when the necessary information is provided.

In some cases, you may receive a request you do not want to accept.  Perhaps the request does not align with the project scope or vision.  It is important to tactfully handle contributions that do not meet the project standards.For example, you could:

* Acknowledge the person behind the contribution and thank them for their interest and help.
* Explain why it did not fit into the scope of the project or vision.
* Do not leave an unwanted contribution open.  Immediately close the contribution you do not wish to accept.
