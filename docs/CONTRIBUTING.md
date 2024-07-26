# How to contribute

Become one of the contributors to this project! We thrive to build a welcoming and open community for anyone who wants to use the project or contribute to it. There are just a few small guidelines you need to follow. To help us create a safe and positive community experience for all, we require all participants to adhere to the [Code of Conduct](https://github.com/dell/ansible-powermax/blob/main/docs/CODE_OF_CONDUCT.md).

## Table of contents

* [Become a contributor](#Become-a-contributor)
* [Submitting issues](#Submitting-issues)
* [Triage issues](#Triage-issues)
* [Your first contribution](#Your-first-contribution)
* [Branching](#Branching)
* [Signing your commits](#Signing-your-commits)
* [Pull requests](#Pull-requests)
* [Code reviews](#Code-reviews)
* [TODOs in the code](#TODOs-in-the-code)

## Become a contributor

You can contribute to this project in several ways. Here are some examples:

* Contribute to the Ansible modules for Dell PowerMax documentation and codebase.
* Report and triage bugs.
* Feature requests.
* Write technical documentation and blog posts, for users and contributors.
* Help others by answering questions about this project.

## Submitting issues

All issues related to Ansible modules for Dell PowerMax, regardless of the service/repository the issue belongs to, should be submitted [here](https://github.com/dell/ansible-powermax/issues). Issues will be triaged and labels will be used to indicate the type of issue. This section outlines the types of issues that can be submitted.  

### Report bugs

We aim to track and document everything related to Ansible modules for Dell PowerMax through the Issues page. The code and documentation are released with no warranties or SLAs and are intended to be supported through a community driven process.

Before submitting a new issue, make sure someone has not already reported the problem. Look through the [existing issues](https://github.com/dell/ansible-powermax/issues) for similar issues.

Report a bug by submitting a [bug report](https://github.com/dell/ansible-powermax/issues/new?labels=type%2Fbug%2C+needs-triage&template=bug_report.md&title=%5BBUG%5D%3A). Ensure that you provide as much information as possible on how to reproduce the bug.

When opening a bug, you need to include this information to help with debugging:

1. Version of relevant software: this software, Ansible, Python, SDK, so on.
2. Details of the issue explaining the problem: what, when, and where.
3. The expected outcome that was not met (if any).
4. Supporting troubleshooting information. __Note: Do not provide private company information that could compromise your company's security.__

An Issue __must__ be created before submitting any pull request. Any pull request that is created should be linked to an Issue.

### Feature request

If you have an idea of how to improve this project, submit a [feature request](https://github.com/dell/ansible-powermax/issues/new?labels=type%2Ffeature-request%2C+needs-triage&template=feature_request.md&title=%5BFEATURE%5D%3A).

### Answering questions

If you have a question and you cannot find the answer in the documentation or issues, the next step is to submit a [question.](https://github.com/dell/ansible-powermax/issues/new?labels=type%2Fquestion&template=ask-a-question.md&title=%5BQUESTION%5D%3A)

We would love your help answering questions being asked by other users of Ansible modules for Dell PowerMax.

## Triage issues

Triage helps resolve issues quickly by:

* Ensuring the intent of the issue and purpose is conveyed precisely. This is necessary because it can be difficult for an issue to explain how an end user experiences a problem and what actions they took.
* Giving a contributor the information they need before they commit to resolving an issue.
* Lowering the issue count by preventing duplicate issues.
* Streamlining the development process by preventing duplicate discussions.

If you do not have the knowledge or time to code, consider helping with _issue triage_. The Ansible modules for Dell PowerMax community thanks you for saving them time by spending some of yours.

Read more about the ways you can [Triage issues](https://github.com/dell/ansible-powermax/blob/main/docs/ISSUE_TRIAGE.md).

## Your first contribution

Unsure where to begin contributing? Start by browsing issues labelled `beginner friendly` or `help wanted`.

* [Beginner-friendly](https://github.com/dell/ansible-powermax/issues?q=is%3Aopen+is%3Aissue+label%3A%22beginner+friendly%22) issues are generally straightforward to complete.
* [Help wanted](https://github.com/dell/ansible-powermax/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22) issues are problems we would like the community to help us with regardless of complexity.

When you are ready to contribute, it is time to create a pull request.

For information about branching, see 
## Branching

* [Branching Strategy for Ansible modules for Dell PowerMax](https://github.com/dell/ansible-powermax/blob/main/docs/BRANCHING.md)

## Signing your commits

We require that developers sign off their commits to certify that they have permission to contribute the code in a pull request. This way of certifying is commonly known as the [Developer Certificate of Origin (DCO)](https://developercertificate.org/). We encourage all contributors to read the DCO text before signing a commit and making contributions.

GitHub prevents a pull request from being merged if there are any unsigned commits.

### Signing a commit

GNU Privacy Guard(GPG) is used to sign commits.  Follow the instructions [here](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/signing-commits) to create a GPG key and configure your GitHub account to use that key.

Ensure that you have your user name and e-mail registered.  These credentials are required for your signed commit to be properly verified.  See these references for more information about setting up your account:

* Setting up your GitHub user name [reference](https://help.github.com/articles/setting-your-username-in-git/)
* Setting up your e-mail address [reference](https://help.github.com/articles/setting-your-commit-email-address-in-git/)

Once Git and your GitHub account have been properly configured, you can add the -S flag to the Git commits:

```console
$ git commit -S -m your commit message
# Creates a signed commit
```

### Commit message format

Ansible modules for Dell PowerMax uses the guidelines for commit messages outlined in [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

## Pull requests

If this is your first time contributing to an open-source project on GitHub, make sure you read about [Creating a pull request](https://help.github.com/en/articles/creating-a-pull-request).

A pull request must always link to at least one GitHub issue. If that is not the case, create a GitHub issue and link it.

To increase the chance of having your pull request accepted, make sure your pull request follows these guidelines:

* Title and description correspond to the implementation.
* Commits within the pull request follow the formatting guidelines.
* The pull request closes one related issue.
* The pull request contains necessary tests that verify the intended behavior.
* If your pull request has conflicts, rebase your branch onto the main branch.

If the pull request fixes a bug:

* The pull request description must include `Fixes #<issue number>`.
* To avoid regressions, the pull request should include tests that replicate the fixed bug.

The team _squashes_ all commits into one when we accept a pull request. The title of the pull request becomes the subject line of the squashed commit message. We still encourage contributors to write informative commit messages, as they becomes a part of the Git commit body.

We use the pull request title when we generate change logs for releases. As such, we strive to make the title as informative as possible.

Ensure that the title for your pull request uses the same format as the subject line in the commit message.

### Quality gates for pull requests

GitHub Actions are used to enforce quality gates when a pull request is created or when any commit is made to the pull request. These GitHub Actions enforce our minimum code quality requirement for any code that get checked into the repository. If any of the quality gates fail, it is expected that the contributor will investigate the check log, understand the problem, and resolve the issue. If help is needed, reach out to the maintainers of the project for [support](https://github.com/dell/ansible-powermax/blob/main/docs/SUPPORT.md).

#### Code sanitization

[GitHub action](https://github.com/dell/ansible-powermax/actions/workflows/ansible-test.yml) that analyzes source code to flag ansible sanity errors and runs Unit tests.

## Code reviews

All submissions, including submissions by project members, require review. We use GitHub pull requests for this purpose. Consult [GitHub Help](https://help.github.com/articles/about-pull-requests/) for more information on using pull requests.

A pull request(PR) must satisfy following criteria:

* A pull request will require at least 2 maintainer approvals.
* Maintainers must perform a review to ensure that the changes adhere to guidelines laid out in this document.
* If any commits are made after the PR has been approved, the PR approval will automatically be removed and the above process must happen again.

## Code style

Ensure that the added code has the required documentation, examples, and unit tests.

### Sanity

Run ansible-test sanity --docker default on your code to ensure sanity. Ensure that the code does not have any Andersson script violations and not break any existing unit test workflows.

### TODOs in the code

We do not like TODOs in the code or documentation. It is best if you sort out all issues you can see with the changes before we check-in the changes.
