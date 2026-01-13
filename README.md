# AI Agents for Social Science and Society 2026

Course Repository for AI Agents for Social Science & Society, Winter 2026

**Instructor:** James A. Evans

**TAs:**
- Jesse Zhou
- Shiyang Lai
- Avi Oberoi
- Gio Choi

## I. The Course
AI agents are emerging everywhere, from social media and the workplace to social science. Agentic AI architectures, powered by large language and vision models atop transformers, trained on a deluge of digital content from the web, can reproduce rich traces of human communication and connection, enabling the creation of intelligent agents now entering the social world as assistants, workers, managers, companions, and more. Such AI agents can also serve as social science research assistants (RAs), collaborators, simulated human subjects, real (AI agent) subjects, theory consultants, and even constitute entire artificial societies for social science inquiry. Because AI agents are not always true to the human persons they are designed to model and assist, we will explore how to correct for their errors, redesign them with new experiences, incentives, and constraints, avoid their use when misleading or harmful, and consider the impacts of their (in)humanity on the human world with whom they interact.
This course takes the position that AI agents represent a fundamental transformation in both society and social science methodology: from cartoons of social life to another dimension of sociality, and from tools that merely process data to autonomous systems that can formulate hypotheses, conduct literature reviews, design studies, analyze complex multimedia data, engage in theoretical reasoning, simulate human behavior and social dynamics, and reveal their own behaviors that are playing an increasingly important role in the human world. In this course, students will learn to understand and construct AI agents that serve as research assistants (automating data collection and analysis), research subjects (simulating human responses and social processes or revealing their own authentic behavior), research advisors (synthesizing literature and proposing theoretical frameworks), research scientists (generating and testing hypotheses), and workers within virtual organizations, members of online institutions, and denizens of artificial societies designed for work, life, or study.
From the perspective of AI agents, everything can be viewed as input and output—novels, field notes, photographs, networks of interaction, survey responses, theories, and research designs. Our treatment examines how to configure agent architectures, multi-modal reasoning pipelines, and tool-using systems to create AI organizations, societies, collaborators, subjects, labs, etc. that could augment society and social scientists’ capacity to ask questions, generate insights, and explore counterfactual scenarios at new scales.
This class is for anyone wishing to build AI systems that can autonomously analyze textual, image, video, or arbitrary structured and unstructured data; engage in complex reasoning about social and cultural phenomena; simulate individual behavior and collective dynamics; and serve as interactive research partners for addressing substantial social and cultural questions, such as how to model cultural evolution, predict ideological shifts, simulate policy interventions, generate ethnographic interpretations, etc..
The course uses Python and the widely popular PyData ecosystem alongside modern AI agent frameworks to demonstrate all motivating examples and includes working code, accompanying exercises, relevant datasets, and methods for evaluating agent reliability and interpretability. Familiarity with Python is required.

**By the end of this class the student will understand:**
- How AI agents build upon traditional deep learning models and why they enable new research paradigms
- Agent architectures: reasoning loops, tool use, memory systems, and multi-agent coordination
- How to design agents that act as research assistants, subjects, advisors, and scientists
- Methods for creating simulated organizations, societies and agent-based models of social phenomena
- Techniques for ensuring agent reliability, reducing hallucinations, and validating agent-generated insights
- Ethical considerations in using AI agents in society and for social science research
- How to navigate the PyData and AI agent ecosystem to build strategic research infrastructure

**And the student will be able to:**
- Design and deploy agents that simulate human subjects for theoretical exploration and counterfactual analysis
- Build multi-agent systems that model social interactions, collective behavior, and cultural dynamics
- Integrate diverse data sources (text, images, sensors) into agent knowledge bases
- Construct agents that use tools (APIs, databases, visualization libraries) to conduct autonomous research
- Evaluate agent outputs for validity, bias, and alignment with research objectives
- Prompt and fine-tune agents for domain-specific social science tasks
- Design human-agent collaboration workflows for rigorous experimentation
- Do all of this in the rich PyData and AI agent ecosystem with code examples for every session

## II. Readings and Computational Tools

Readings will be circulated in class and through the course’s Canvas site.

Computational tools required to fulfill the exploration assignments are modeled in python, and will most easily be replicated and extended in python. Students must perform weekly homework in the course within notebooks students can download online and run from their own computers, run from the Research Computing Center’s machines, or using a Google Colab notebook (we recommend upgrading to a Pro account). Moreover, the course has special access to a grant from Anthropic and AWS, which gives us access to Claude Code credits that enables students to build facility with AI coding agents that students are encouraged to use to perform homeworks and build impressive final projects.

The course's code and any other helper material will be found on the course GitHub repository.

## III. Course Requirements

The course will be held in person, Friday 1:30-4:20pm. Class will take place in 1155 E. 59th Street, 295, where I will share a short lecture, students will share coding presentations (see below); I will answer the most upvoted questions about the readings (see below), and students will perform some coding and analysis in group projects.

Prior to the first session, all registered students are required to complete the data disclosure form and pre-class survey posted here. This process should take approximately 15–20 minutes.

### A. Reading, Memo, & Presentations (30%)

Participation is expected of all class members. Students are expected to read and reflect on all "required" readings each week, and one or more "supplemental" readings. Students should be prepared with a question about the reading they are encouraged to ask the instructor in class, and the TAs and each outside it.

**Memos:** Each week (starting week 2), students will post a memo that explores the reading and class topics relevant to your final project on AI agents for social science and society to our course GitHub site (also accessible through Canvas) by Thursday @ midnight prior to our Friday Class. By 10am Friday, each student will up-vote ("thumbs up") what they think are the five most interesting memos for that week. The memo should be 300–500 words and include the following:
1. State your research question (for the imagined final project) succinctly in a single sentence at the beginning (this can and should evolve across the weeks of the quarter as the project becomes more concrete)
2. Propose a research design that helps to address that question, and not proposed in any prior memo, informed by at least one of the required readings and one of the supplemental readings from the week
3. A visual figure or diagram that draws upon pilot (non-hallucinated) data, simulated data with defensible assumptions, or provides a clear conceptual illustration that persuades the reader (aka me and TAs) of the appropriateness and fruitfulness of the design to address your question

Students will then pilot this design as the final question in the homework due the following Wednesday. Students are encouraged to use agentic AI for writing/coding as helpful, but will be fully accountable for their memos and associated proposals. Even if students are involved in a group project, and their question is shared, the memos are separate and should reflect distinct research design explorations and possibilities. The Instructor and TAs will randomly some of these visuals in class and Lab sessions for students to spontaneously describe. Some of the top- and bottom-voted memos may also form the backbone of our class discussion sessions.

**Code Presentation:** Once per quarter, students will also sign-up to perform a 5-minute discussion of their personal weekly exercises (described below), focusing on preliminary (juicy) results related to their (imagined) project using the Jupyter notebook code and requested extensions. The presentation will focus on analysis outputs, visualizations and content-driven stories. This is also to be presented in Ignite Talk format, where slides should include interesting screenshots from your Jupyter notebook homework assignment. Presentations will occur on Fridays @ 1:30pm. All presenting students will post 20-PDF slide decks prior to class. In the online sign-up (Google Sheets) linked from the Canvas course home page here, sign up for "Student 1-3" slots for findings presentations before signing up for higher numbered slots. The critical thing here is that there are at least three student code examples each week. A few notes: These are NOT group presentations. Students are just presenting the most interesting discoveries made in the course of doing their homework. Also note, on the week that students do their code presentations they require doing their homework 5 days early because they are performing discoveries based on homework that will not be due for the rest of the class until the following Wednesday. I encourage students sign-up for these early in the quarter…earlier is easier ;-). Student slides must be uploaded by Friday @ 1pm for presentation that day. The reading and discussion grade will be a function of memos graded, up-votes received, and the quality of code and memo presentations.

### B. Weekly Exercises (35%)

Tuesday of each week, we will publish a Jupyter interactive Python notebook containing code examples and requested extensions associated with the AI agent skills we are learning that week. Students are expected to have familiarized themselves with the code before class to facilitate exploration with their own corpus during class. 

Students are expected to complete a weekly homework intended to invite experimentation with the techniques we consider. Homework will consist of performing all operations and requested extensions from the published notebook on a corpus or corpora associated with students' anticipated final projects (see below). In going through the homework, we invite students to alter parameters, inputs and outputs. At several structured points, we will ask questions that stimulate final group projected students to:
1. Summarize results from preliminary analysis using deep learning methods associated with your (e.g., with text and graphics or succinct tables)
2. Identify and interpret examples from data that facilitate qualitative validation of the patterns summarized
3. Critically evaluate the approach's drawbacks and scope conditions for its beneficial deployment

As noted earlier, six students will sign-up to prepare the substance of these assignments and lead a discussion about their results before the assignments are formally due.

Student notebooks must be pushed by noon on Wednesday following the relevant week of class (although some students will have presented results from this assignment on the Friday before). Students are encouraged to work on these assignments in groups (although you will turn them in individually) and to key assignments to the substance of the final group project.

There will be a rotating Lab section devoted to helping students with code-relevant assignments led by the TA involved in the development and/or refinement of that week's code. It will take place during the first hour of that TAs weekly office hour (for in-person attendance), and will be recorded and uploaded through canvas for student who cannot attend.

Upon completing each weekly tutorial and memo, you are required to submit a brief post-assignment survey. This survey tracks your use of Claude Code and other AI assistants, as well as your feedback on the assignment. Your responses help us evaluate the effectiveness of these tools and refine the course design for future semesters.

Grading for homework and memos will be performed using a 0 (didn't turn in) to 10 (fabulous) point scale. I will drop all but the highest 6 homework grades over the course of the quarter for full credit.

### C. Final Project (35%)

Students will work alone or in groups (of up to 4) to perform a substantial AI agent project for social insight based on approaches and tools developed/explored over the course of the quarter. These projects must integrate at least three forms of data in a single model, use at least three types of models (from three separate weeks over the course of the quarter), and must validate inferences or predictions with qualitative interpretation and assessments. These projects are encouraged to be performed in groups (of up to 4 students). Examples include†:
 
1. **Social Media Behavior and Platform Dynamics:** Analysis of content moderation, misinformation spread, and community formation on platforms like Reddit, Twitter/X, or TikTok, integrating text (posts, comments, captions), social networks (follower/following graphs, reply chains, repost cascades), and tabular data (engagement metrics, posting frequency, account age) with AI research assistance for classification and pattern detection, or with AI agents simulating user behavior under alternative platform designs (e.g., friction interventions, algorithmic feed changes), or experiments pairing human moderators with AI assistants to evaluate content.

2. **Urban Mobility and Crime Patterns:** Investigation of how urban movement patterns relate to crime incidence and neighborhood change, combining text (311 reports, police blotters, news coverage, Yelp reviews), spatial networks (transit connectivity, pedestrian flows, crime co-occurrence), and tabular data (rideshare pickups, foot traffic sensors, crime statistics, demographic indicators) with AI research assistance for anomaly detection and causal inference, or with AI agents simulating resident and offender mobility decisions under counterfactual urban interventions (e.g., new transit lines, streetlight placement), or human-AI teams conducting virtual ethnography of neighborhood dynamics.

3. **Consumer Commerce and Market Dynamics:** Study of supply-demand matching, price discovery, and consumer preference formation in online marketplaces (Amazon, Etsy, eBay, StockX), integrating text (product descriptions, reviews, seller communications), bipartite networks (buyer-seller transactions, product co-purchase graphs), and tabular data (prices, inventory, ratings, shipping times) with AI research assistance for demand forecasting and preference extraction, or with AI agents simulating buyer and seller strategies under different market structures or information conditions, or experiments with human sellers assisted by AI pricing and inventory agents.

4. **Political Opinion Dynamics and Polarization:** Examination of attitude formation, polarization trajectories, and cross-partisan interaction on political forums, comment sections, or survey panels, combining text (political posts, comments, survey open-ends), social networks (interaction graphs, co-exposure networks, citation patterns among political sources), and tabular data (voting records, demographic covariates, sentiment time series) with AI research assistance for stance detection and trajectory clustering, or with AI agents simulating voter opinion updating under alternative media environments or social network structures, or deliberation experiments pairing human participants with AI interlocutors holding calibrated opposing views.
5. **Scientific Idea Diffusion and Evolution:** Analysis of how concepts, methods, and theories spread and transform across scientific communities, integrating text (abstracts, full papers, grant proposals, peer reviews), citation and collaboration networks (co-authorship, citation flows, institutional mobility), and tabular data (funding amounts, publication counts, altmetrics, replication outcomes) with AI research assistance for novelty measurement and lineage tracing, or with AI agents simulating researchers making reading, citing, and collaboration decisions under alternative incentive structures (e.g., open access regimes, preregistration mandates), or human-AI teams conducting systematic reviews or hypothesis generation.

6. **Complex vs. Simple Contagion in Social Networks:** Investigation of threshold-dependent adoption processes for behaviors, beliefs, or innovations, combining text (adoption narratives, persuasion attempts, testimonials), network data (friendship ties, communication logs, geographic proximity), and tabular data (adoption timing, demographic attributes, prior behavior) with AI research assistance for distinguishing contagion mechanisms from homophily, or with AI agents simulating adoption decisions under varied network topologies and threshold distributions, or field experiments where AI agents serve as early adopters or bridge nodes to test contagion dynamics.

7. **Emotional Contagion in Interaction:** Study of how affect spreads through dyadic and group conversation, integrating text (chat logs, transcripts, social media threads), temporal interaction networks (turn-taking sequences, response latencies, conversation graphs), and multimodal signals (sentiment trajectories, emoji usage, acoustic features if available) with AI research assistance for emotion detection and cascade identification, or with AI agents simulating conversational partners with calibrated emotional profiles to test contagion hypotheses, or human-AI interaction experiments measuring how AI emotional tone influences human affective states and downstream behavior.

8. **Grassroots Mobilization and Collective Action:** Examination of how protest movements, petitions, or mutual aid networks form and sustain participation, combining text (organizing posts, petition language, news coverage), mobilization networks (event co-attendance, sharing cascades, organizational affiliations), and tabular data (petition signatures over time, protest attendance, donation flows) with AI research assistance for framing analysis and tipping point detection, or with AI agents simulating potential participants making costly participation decisions under varying information and social pressure, or experiments testing AI-generated mobilization appeals against human-crafted alternatives.
9. **Cultural Taste and Aesthetic Evolution:** Analysis of how preferences for music, visual art, fashion, or cuisine form, cluster, and shift over time, integrating text (reviews, critiques, artist statements, social commentary), bipartite consumption networks (listener-artist, viewer-artwork, diner-restaurant), and tabular/image data (streaming counts, visual features, trend indices) with AI research assistance for taste clustering and novelty scoring, or with AI agents simulating consumers navigating recommendation systems under alternative curation algorithms, or human-AI co-creation experiments where AI generates aesthetic variations and humans provide preference feedback.

10. **Organizational Communication and Decision-Making:** Study of how information flows, decisions emerge, and culture forms within organizations, combining text (Slack messages, email threads, meeting transcripts, internal documents), communication networks (who-talks-to-whom graphs, reporting structures, cross-team collaboration), and tabular data (project outcomes, employee tenure, performance metrics) with AI research assistance for bottleneck detection and sentiment dynamics, or with AI agents simulating organizational members under alternative hierarchy or communication structures, or human-AI team experiments where AI serves as meeting facilitator, devil's advocate, or information synthesizer to test effects on decision quality.

Specific datasets or access associated with some possible example projects are described on the following page (make suggestions if you find other valuable data). Please fill out the following form to express your interest in a group project.

Groups will compose a detailed, entertaining, and informative public-facing Substack or Medium.com blog post about their projects that includes the motivation, methodological justification and details, descriptive data and deep learning modeling, interpretation of findings (e.g., discovered structures, predictions, generations), conclusion, and an annotated code appendix. These should not read like an academic paper, but a mixture of (1) explanatory tutorial; and (2) digital museum exhibit, balancing intermittent text with figures, description boxes, equations, and/or conceptual diagrams including at least one visual element (e.g., figure, graph, conceptual diagram) for every 300 words of text; and a minimum total of 5000 words and 17 visual elements; but 3600 words and 13 visual elements for single author projects. In short, they represent the methods section + operational tutorial of a (hopefully) awesome paper. These may include relevant code and should link to an open GitHub or Colab repository for code evaluation. Posts are due Friday, Mar 14th @ 5pm. Groups will also present the motivation, process and findings from their projects the day before in slots log-proportional to the size of the team (5 minutes/20 slides for 1-person teams; 6.5 minutes/26 slides for 2-person teams; 7.5 minutes/30 slides for 3-person teams; 8 minutes/32 slides for 4-person teams; 8.5 minutes/34 slides for 5-person teams) online Ignite style talks on Wednesday, Mar 11th from 5:00pm. Students will submit (1) final presentation slides by Wednesday, Mar 11 @ 3:00pm (sign up for presentations here).

† Students with data connected to a personal project (e.g., related to a thesis or dissertation) may work on projects alone or in smaller groups with instructor authorization.

## IV. Calendar of Reading Assignments

### Week 0. Whenever: Recommended Introduction / Review

**Programming**
- General Python Tutorial: https://docs.python.org/3/tutorial/
- "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering." Yang, J., Jimenez, C. E., Wettig, A., et al. arXiv. 2024.

**Mathematics**
- "Linear Algebra" and "Probability and Information Theory", Deep Learning, chapters 2-3.
- Something else?

**Claude Code Setup**
- Tutorial to setup on Canvas

### Week 1. Jan. 9: Deep Learning and Social Agents

In this introductory week, we define Neural Networks, deep and shallow, and examine the relationship between deep learning, traditional approaches to statistical learning, and the possibility of and potential for agent models in social science and society.

**Required**
- AI Foundations: "Preface: How to Think with Deep Learning", "Deep Learning?", "Training and Taming Deep Networks". Thinking with Deep Learning, Preface, Chapter 1, Chapter 3. James Evans.
- "Exploring Large Language Model Based Intelligent Agents: Definitions, Methods, and Prospects." Yuheng Cheng et al. preprint. 2025.
- "Sparks of Artificial General Intelligence: Early experiments with GPT-4." S. Bubeck, V. Chandrasekaran, R. Eldan, et al. Microsoft Research. 2023.
- Social Perspectives: "Large AI Models are Cultural and Social Technologies." Science 387(6739):1153-1156. Farrell, Henry, Alison Gopnik, Cosma Shalizi, James Evans. 2025.
- Social Designs: "Generative Agents: Interactive Simulacra of Human Behavior." J. S. Park, J. C. O'Brien, C. J. Cai. UIST. 2023.

**Supplemental**
- AI Foundations: "Introduction", "Deep Neural Networks", "Gradient Descent", "Backpropagation", and "Regularization" Deep Learning: Foundations and Concepts, Springer-Nature. Chapters 1, 6-10. Christopher and Hugh Bishop. 2025.
- "Foundations" and "Fundamentals", Deep Learning from Scratch, chapters 1-2. Seth Weidman. 2024.
- AI Designs: "Introduction to Artificial Neural Networks with Keras", Hands-On Machine Learning with Scikit-Learn, Keras & Tensorflow, chapter 10. Aurelien Geron. 2024.
- "Getting Started with PyTorch", Programming PyTorch for Deep Learning, chapter 1.
- "Training Deep Networks", Hands-On Machine Learning with Scikit-Learn, Keras & Tensorflow, chapter 11.
- AI Perspectives: "The unreasonable effectiveness of deep learning in artificial intelligence". 2020. Terrence J. Sejnowskia. Proceedings of the National Academy of Sciences.
- "Reducing the Dimensionality of Data with Neural Networks", Hinton, G. E., Salakhutdinov, R. R., 2006. Science 313(5786):504-507.
- "A Unified Approach to Interpreting Model Predictions". 2017. S. Lundberg and Su-In Lee. NeurIPS.
- Philosophical Perspectives: "Minds, brains, and programs." 1980. Searle, John R. Behavioral and brain sciences, 3(3), 417-424.
- "Utterer's meaning and intention" 1969. Grice, H. Paul. The philosophical review, 78(2), 147-177.
- "Intentional systems" 1971. Dennett, Daniel C. The journal of philosophy, 68(4), 87-106.
- Social Designs: "Online Images Amplify Gender Bias". 2024. Douglas Guilbeault, Solène Delecourt, Tasker Hull, Bhargav Srinivasa Desikan, Mark Chu & Ethan Nadler. Nature 626:1049–1055.
- "Using sequences of life-events to predict human lives". 2023. Germans Savcisens, Tina Eliassi-Rad, Lars Kai Hansen, Laust Hvas Mortensen, Lau Lilleholt, Anna Rogers, Ingo Zettler & Sune Lehmann. Nature Computational Science 4: 43–56.
- "Machine learning for pattern discovery in management research". (2020).

**Lab session:** Avi Oberoi, Tuesday, 11-12am

### Week 2. Jan. 16: Text Learning, Transformers, and Diffusion Models

This week we survey deep neural networks for human meaning from text, beginning with shallow text networks (e.g., word2vec) to transformer and diffusion models. We will discuss chain, tree, and graph of thought reasoning within these models to facilitate “self-talk” for reflective behavior, reasoning, and action.

**Required**
- AI Foundations/Techniques: "Attention Is All You Need." Vaswani, A., Shazeer, N., Parmar, N., et al. NeurIPS. 2017.
- "Transformers and Pre-trained Language Models" Jurafsky & Martin, Speech and Language Processing (3rd ed. draft), Chapter 10. 2023.
- Social Perspectives: "Cultural tendencies in generative AI" Lu, Jackson G., Lesley Luyang Song, and Lu Doris Zhang. Nature Human Behaviour (2025)
- Social Designs: "Language Model Perplexity Predicts Scientific Surprise and Transformative Impact". Zhen Zhang and James Evans (2025)

**Supplemental**
- AI Foundations: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." Wei et al. NeurIPS (2022)
- "Let's Verify Step by Step." Lightman, H., Kosaraju, V., Burda, Y., et al. OpenAI. 2023.
- "Transformer Circuits Thread". Anthropic Interpretability Group (2025)
- "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." Yao, S., Yu, D., Zhao, J., et al. NeurIPS. 2023.
- AI Interpretability: "Neuronpedia: Interactive reference and tooling for analyzing neural networks". Lin, J., & Bloom, J. (2023)
- "A mathematical theory of semantic development in deep neural networks" Andrew M. Saxe, James L. McClelland, and Surya Ganguli. PNAS (2019)
- "What is ChatGPT doing… and why does it work?" Stephen Wolfram. Informal explanation of analysis.
- "Mapping Overlaps in Benchmarks with Perplexity in the Wild". Wu, S., Bao, H., Li, S., Holtzman, A., and Evans, J. 2025
- "The clock and the pizza: Two stories in mechanistic explanation of neural networks" 2023. Zhong, Z., Liu, Z., Tegmark, M., & Andreas, J. NeurIPS, 36, 27223-27250.
- Social Perspectives: "The Geometry of Culture: Analyzing the Meanings of Class through Word Embeddings" A. Kozlowski, M. Taddy, J. Evans. American Sociological Review (2019)
- "Who Sees the Future? A Deep Learning Language Model Demonstrates the Vision Advantage of Being Small" P Vicinanza, A. Goldberg, S. Srivastava. PNAS Nexus (2022)
- Social Designs: "Large Language Models for Computational Social Science: A Survey." Fengli Xu, Chenyang Shao, Lin Chen, Qingbin Zeng, Zhilong Chen, Nicholas Sukiennik, Jingyi Wang, Chen Gao, Huandong Wang, Jianxun Lian, Qingguo Meng, Xing Xie, Yong Li, James Evans. 2026.

**Lab Session:** Shiyang Lai, Wednesday, 2-3pm

### Week 3. Jan. 23: LLMs Prompted for Multi-Agent Simulation

This week, we explore the potential of transformer-based large language models for creating “digital doubles” that enable predictive simulation of the social and cultural actors and scenarios you seek to investigate, enabling their interrogation for deeper understanding about the social and cultural world, and their simulated interaction to perform social science in silico. 

**Required**
- AI Foundations/Techniques: “Simulating Subjects: The Promise and Peril of AI Stand-ins for Social Agents and Interactions” by Austin C. Kozlowski and James A. Evans. 
- Social Perspectives: “From Predictive Pattern Completion to Social and Cultural Norms.” Joel Z. Liebo, Alexander Sasha Vezhnevets, Manfred Diaz, John P. Agapiou, William A. Cunningham, Peter Sunehag, Logan Cross, Raphael Koster, Stanfley Mileschi, Minsuk Chang, Iyad Rahwan, Simon Osindero, and James Evans. 2025.
- Social Designs: “Subjective Perspectives within Learned Representations Predict High-Impact Innovation.” Cao, Likun, Rui Pan, James Evans. 
- “Using large language models to categorize strategic situations and decipher motivations behind human behaviors.” Yutong Xie, Qiaozhu Mei, Walter Yuan, and Matthew O. Jackson. PNAS 122 (35) e2512075122
- “The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies.” Kyle Swanson, Wesley Wu, Nash L. Bulaong, John E. Pak & James Zou. Nature. 2025.
**Supplemental**
- AI Foundations: “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks”. Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela. 2021.
- AI Perspectives:  “Transformers learn in-context by gradient descent.” Johannes von Oswald, Eyvind Niklasson, Ettore Randazzo, João Sacramento, Alexander Mordvintsev, Andrey Zhmoginov, Max Vladymyrov. 2024.
- AI Designs: LangGraph (LangChain-based agent system)
- “Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia”. 2023. Vezhnevets, A. S., Agapiou, J. P., Aharon, A., Ziv, R., Matyas, J., Duéñez-Guzmán, E. A., ... & Leibo, J. Z.
- “Autogen: Enabling next-gen llm applications via multi-agent conversation framework”. 2023. Wu, Q., Bansal, G., Zhang, J., Wu, Y., Zhang, S., Zhu, E., ... & Wang, C.
- “AFlow: Automating Agentic Workflow Generation” Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xionghui Chen, Jiaqi Chen, Mingchen Zhuge, Xin Cheng, Sirui Hong, Jinlin Wang, Bingnan Zheng, Bang Liu, Yuyu Luo, Chenglin Wu. 2025.
- The Faiss library (vector library). Matthijs Douze, Alexandr Guzhva, Chengqi Deng, Jeff Johnson, Gergely Szilvasy, Pierre-Emmanuel Mazaré, Maria Lomeli, Lucas Hosseini, Hervé Jégou. 2024.
- “A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges.” Li, X., Wang, S., Zeng, S., Wu, Y., & Yang, Y. 2024.
- “Large language model based multi-agents: A survey of progress and challenges.” Guo, T., Chen, X., Wang, Y., Chang, R., Pei, S., Chawla, N. V., ... & Zhang, X. 2024.
- “The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery” by C. Lu, C. Lu, R. Tjarko Lange, J. Foerster, J. Clune, and D. Ha. 2024.
- “The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search” Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, David Ha. 2025.
- “A Survey of AI Scientists” Tie, G., Zhou, P., & Sun, L. 2025.
- “AI for social science and social science of AI: A survey. ” Xu, R., Sun, Y., Ren, M., Guo, S., Pan, R., Lin, H., ... & Han, X. 2024.
- “Many heads are better than one: Improved scientific idea generation by a llm-based multi-agent system.” Su, H., Chen, R., Tang, S., Yin, Z., Zheng, X., Li, J., ... & Dong, N. ACL. 2025.
- Social Perspectives: “Out of one, many: Using language models to simulate human samples.” Argyle, Lisa P., Ethan C. Busby, Nancy Fulda, Joshua R. Gubler, Christopher Rytting, and David Wingate. 2023. Political Analysis. 
- “Virtual Agent Economies.” Tomasev, N, Franklin, M, Leibo, J.Z., Jacobs, J., Cunningham, W.A., Gabriel, I., Osindero, S. Preprint. 2025.
- “War and Peace (WarAgent): Large Language Model-based Multi-Agent Simulation of World Wars.” Hua, W., Fan, L., Li, L., et al. arXiv. 2023.
- “Why do multi-agent llm systems fail?” 2025. Cemri, Mert, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer et al. arXiv.
- “Emergent Convergence in Multi-Agent LLM Annotation.” 2025. Angelina Parfenova, Alexander Denzler, Jürgen Pfeffer. In Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP, pages 206–225.
- Social Designs: “In Silico Sociology: Forecasting COVID-19 Polarization with Large Language Models” by Austin C. Kozlowski, Hyunku Kwon, and James A. Evans.
- “Emergence of human-like polarization among large language model agents.” Piao, Jinghua, Zhihong Lu, Chen Gao, Fengli Xu, Fernando P. Santos, Yong Li, James Evans.
- “Simulating social media using large language models to evaluate alternative news feed algorithms.” Törnberg, Petter, Diliara Valeeva, Justus Uitermark, and Christopher Bail. 2023. arXiv.

**Lab Session:** Gio Choi, Thursday 2-3pm


### Week 4: Jan. 30: Experimental Designs with AI Agent and Human Interactions 

This week, we explore experimental designs and causal identification for social analysis with AI agents.

**Required**
- Social Designs: "The Mixed Subjects Design: Treating Large Language Models as Potentially Informative Observations" Broska, D., Howes, M., & van Loon, A. Sociological Methods & Research, 00491241251326865. 2025.
- "Durably reducing conspiracy beliefs through dialogues with AI". Costello, T. H., Pennycook, G., & Rand, D. G. Science, 385(6714), eadq1814. 2024.
- “Hidden Persuaders: How LLM Political Bias Could Sway Our Elections”. Potter, Yujin, Shiyang Lai, Junsol Kim, James Evans, Dawn Song. 2024. Empirical Methods in Natural Language Processing (EMNLP).
- “Biased AI improves human decision-making but reduces trust.” Shiyang Lai, Junsol Kim, Nadav Kunievsky, Yujin Potter, James Evans.
- "Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?" Horton, J. J. NBER Working Paper. 2023.
- "Deep learning for causal inference", Bernard Koch, Tim Sainburg, Pablo Geraldo, Jiang Song, Yizhou Sun, and Jacob G. Foster.

**Supplemental**
- AI Foundations/Designs: “Guidelines for Human-AI Interaction” Saleema Amershi, Dan Weld, Mihaela Vorvoreanu, Adam Fourney, Besmira Nushi, Penny Collisson, Jina Suh, Shamsi Iqbal, Paul N. Bennett, Kori Inkpen, Jaime Teevan, Ruth Kikin-Gil, Eric Horvitz. 2019.
- Social Designs: "Double/Debiased Machine Learning for Treatment and Causal Parameters". 2018. Victor Chernozhukov, et al. C1-C68.
- "Deep Neural Networks for Estimation and Inference". 2021. Max H. Farrell, Tengyuan Liang, Sanjob Misra. Econometrica 89(1).
- "Deep Learning for Individual Heterogeneity: An Automatic Inference Framework". Max H. Farrell, Tengyuan Liang, Sanjob Misra. 2022 

**Lab Session:** Jesse Zhu & Shiyang Lai (each will hold a separate session during their hour), 
Monday, 3-4pm (Jesse), Wednesday 2-3pm (Shiyang)


### Week 5. Feb. 6: Sampling, Fine Tuning, Benchmarking, and Tools 

This week we explore the potential for data-driven bias in social scientific inference with AI agents, and how to fine-tune large transformer-based agents to limit bias or adopt specific perspectives. 

**Required**
- AI Foundations: "Advanced Active Learning", Human-in-the-Loop Machine Learning, chapter 1, 4-6 (subset)
- "Sampling" in Deep Learning: Foundations and Concepts, chapter 14.
- AI Designs: “LoRA: Low-Rank Adaptation of Large Language Models.” Edward Hu, Yuanzhi Li, Yelong Shen, Shean Wang, Phillip Wallis, Lu Wang, Zeyuan Allen-Zhu, Weizhu Chen. 2021.
- “Evaluation and benchmarking of llm agents: A survey.” Mohammadi, M., Li, Y., Lo, J., & Yip, W. KDD. 2025.
- “What is the Model Context Protocol (MCP)?” Anthropic. 2024
- AI Perspectives: “AI models collapse when trained on recursively generated data” Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. Nature, 631(8022), 755-759. 2024.
- Social Designs: “Language models trained on media diets can predict public opinion.” E Chu, J Andreas, S Ansolabehere, D Roy. 2023.

**Supplemental**
- AI Foundations: “Active Learning with PyTorch” and “Active Transfer Learning with PyTorch”. Medium posts by Robert Munro. 2019-2020.
- “AI Agents That Matter” Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, Arvind Narayanan. 2024.
- AI Designs: “QLoRA: Efficient Finetuning of Quantized LLMs.” 2023. Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer. 2023.
- “Direct Preference Optimization: Your Language Model is Secretly a Reward Model”. Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn. 2023.
- “Towards scientific intelligence: A survey of llm-based scientific agents.” Ren, S., Jian, P., Ren, Z., Leng, C., Xie, C., & Zhang, J. 2025.
- “Survey on evaluation of llm-based agents.” Yehudai, A., Eden, L., Li, A., Uziel, G., Zhao, Y., Bar-Haim, R., ... & Shmueli-Scheuer, M. 2025.
- “From llm reasoning to autonomous ai agents: A comprehensive review.” Ferrag, M. A., Tihanyi, N., & Debbah, M. 2025.
- “Training Socially Aligned Language Models on Simulated Social Interactions.” Liu, R., Yang, R., Jia, C., et al. ICLR. 2024.
- “AgentBench: Evaluating LLMs as Agents.” Liu, X., Yu, H., Zhang, H., et al. ICLR. 2024.
- “Interactive Debugging and Steering of Multi-Agent AI Systems” Will Epperson, Gagan Bansal, Victor C Dibia, Adam Fourney, Jack Gerrits, Erkang (Eric) Zhu, Saleema Amershi. 2025.
- “DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines”. Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan, Saiful Haq, Ashutosh Sharma, Thomas T. Joshi, Hanna Moazam, Heather Miller, Matei Zaharia, Christopher Potts. 2023.
- “AIOS: LLMAgentOperating System”. Kai Mei, Xi Zhu, Wujiang Xu, Mingyu Jin, Wenyue Hua, Zelong Li Shuyuan Xu, Ruosong Ye, Yingqiang Ge, Yongfeng Zhang. 2025.
- Kubeflow and MLflow HPC pipelines.
- Social Perspectives: “Dissecting racial bias in an algorithm used to manage the health of populations”. Z. Obermeyer, B. Powers, C. Vogeli, S. Mullainathan. Science 366(6464): 447-453. 2019.
- “Semantics derived automatically from language corpora contain human-like biases.” A. Caliskan, J. J. Bryson, A. Narayanan. Science 356(6334):183-186. 2017.
- “Weird Generalization and Inductive Backdoors: New Ways to Corrupt LLMs .” Jan Betley, Jorio Cocola, Dylan Feng, James Chua, Andy Arditi, Anna Sztyber-Betley, Owain Evans. 2025.
- Social Designs: “SciSciGPT: Advancing Human-AI Collaboration in the Science of Science.” Shao, E., Wang, Y., Qian, Y., Pan, Z., Liu, H., & Wang, D. Nature Computational Science. 2025.
- “Curie: Toward rigorous and automated scientific experimentation with ai agents.” Kon, P. T. J., Liu, J., Ding, Q., Qiu, Y., Yang, Z., Huang, Y., ... & Chen, A. 2025.

**Lab Session:** Jesse Zhu, Monday 3-4pm

### Week 6. Feb. 13: Auto-Encoders, Interpretability, and Steering Agents 

This week we investigate how to understand the various contributions of transformer layers to model personas, and how to identify and steer agent qualities underlying them. 

**Required**
- AI Foundations: “Towards Monosemanticity: Decomposing Language Models With Dictionary Learning.” Trenton Bricken, Adly Templeton, Joshua Batson,… Shan Carter, Tom Henighan, Chris Olah. 2023.
- AI Designs: “Sparse Autoencoders Find Highly Interpretable Features in Language Models.” Hoagy 
- Cunningham, Aidan Ewart, Logan Riggs, Robert Huben, Lee Sharkey. 2023.
- Social Designs: “Linear representations of political perspective emerge in large language models”. Kim, J., Evans, J., & Schein, A. ICLR. 2025.
- “Persona vectors: monitoring and controlling character traits in language models”. Chen, R., Arditi, A., Sleight, H., Evans, O., & Lindsey, J. arXiv. 2025.

**Supplemental**
- AI Foundations: “Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet.” Templeton, A., Conerly, T., Marcus, J., Lindsey, J., Bricken, T., Chen, B., ... & Olah, C. Anthropic. 2024.
- “Mapping the Mind of a Large Language Model.” Anthropic. 2024. [Accessible companion to the technical work]
- “A Primer on the Inner Workings of Transformer-based Language Models.” Ferrando, J., Sarti, G., Bisazza, A., & Costa-jussà, M. R. arXiv. 2024.
- AI Designs: “Activation Addition: Steering Language Models Without Optimization.” Turner, A., Thiergart, L., Udell, D., Leech, G., Mini, U., & MacDiarmid, M. arXiv. 2023.
- “Inference-Time Intervention: Eliciting Truthful Answers from a Language Model.” Li, K., Patel, O., Viégas, F., Pfister, H., & Wattenberg, M. NeurIPS. 2023.
- “In-Context Vectors: Making In-Context Learning More Effective and Controllable Through Latent Space Steering.” Liu, S., Lei, C., Huang, X., & Huang, Y. ICML. 2024.
- “Scaling and Evaluating Sparse Autoencoders.” Gao, L., la Tour, T. D., Tillman, H., Goh, G., Troll, R., Radford, A., ... & Wu, J. OpenAI. 2024.
- “Transcoders Find Interpretable LLM Feature Circuits.” Dunefsky, J., Chlenski, P., & Nanda, N. arXiv. 2024.
- Social Designs: “Uncovering Latent Arguments in Social Media Messaging by Employing LLMs-in-the-Loop Strategy.” Fang, H., Lim, A., Chew, R., & Bian, J. arXiv. 2024.
- “Eliciting Human Preferences with LLMs-as-Questionnaires.” Reddy, S., Michael, J., Ziegler, D., et al. arXiv. 2024.

**Lab Session:** Shiyang Lai, Wednesday, 2-3pm


### Week 7. Feb. 20: Reinforcement Learning to Optimize AI Agents and Institutions

Here we introduce reinforcement learning and its uses in agent modeling ranging from RLHF (Reinforcement Learning with Human Feedback) to Reasoning Models to Multi-Agent reinforcement Learning with Collaborative Reward Functions. 

**Required**
- AI Foundations: “Why Reinforcement Learning”, Reinforcement Learning, chapter 1.
- “Reinforcement Learning”, Hands-On Machine Learning with Scikit-Learn, Keras & Tensorflow, chapter 18.
- “Human-level control through deep reinforcement learning” V. Mnih...D. Hassabis.
- Nature 518: 529–533. 2015.
- “Constitutional AI: Harmlessness from AI Feedback.” Bai, Y., Kadavath, S., Kundu, S., et al. Anthropic. 2022.
- AI Techniques: “Training Language Models to Follow Instructions with Human Feedback.” Ouyang, L., Wu, J., Jiang, X., et al. NeurIPS. 2022.
- “DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning.” Guo, D., Yang, D., Zhang, H. et al. Nature 645, 633–638 (2025).
- Social Perspectives: “Reasoning Models Generate Societies of Thought.” Junsol Kim, Shiyang Lai, Nino Scherrer, Blaise Aguera y Arcas, James Evans.
- “On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models” 2025. Zhang, C., Neubig, G., & Yue, X. arXiv. (2025).
- “Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models”
- “RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals”

**Supplemental**
- AI Foundations: “Markov Decision Processes, Dynamic Programming, and Monte Carlo Methods”, Reinforcement Learning, chapter 2.
- “Deep Reinforcement Learning from Human Preferences.” 2017. Christiano et al. NeurIPS.
- AI Perspectives: “Explainability in deep reinforcement learning”. Alexandre Heuilleta, Fabien Couthouis, Natalia Díaz-Rodríguez. 2021.
- AI Techniques: “Agent Lightning: Train ANY AI Agents with Reinforcement Learning” Xufang Luo, Yuge Zhang, Zhiyuan He, Zilong Wang, Siyun Zhao, Dongsheng Li, Luna K. Qiu, Yuqing Yang. 2025.
- OpenPipe/ART Agent Reinforcement Trainer (GRPO code).
- Social Designs“Cognitive behaviors that enable self-improving reasoners, or, four habits of highly effective stars” Gandhi, K., Chakravarthy, A., Singh, A., Lile, N., & Goodman, N. D. (2025).

**Lab Session:** Avi Oberoi, Tuesday, 11-12am


### Week 8. Feb. 27: Multi-Modal and Embodied Agents

This week we build deep neural network agents that can use a range of sensory input and multi-media production, including audio and video. We further consider the challenges and opportunities of embodiment as through robot agents. 

**Required**
- AI Foundations: “Convolutional Neural Networks” and “Diffusion Models” in Deep Learning: Foundations and Concepts, chapters 10 and 20.
- “REACT: Synergizing Reasoning and Acting in Large Language Models.” Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao. 2025.
- AI Designs: “GPT-4V(ision) System Card.” OpenAI. 2023.
- “Embodied Task Planning with Large Language Models.” Song, C. H., Wu, J., Washington, C., et al. arXiv. 2023.
- Social Designs: “Machine Learning as a Tool for Hypothesis Generation”, Jens Ludwig, Sendhil Mullainathan. The Quarterly Journal of Economics 2024. 
- “Age and gender distortion in online media and large language models”. Douglas Guilbeault, Solène Delecourt & Bhargav Srinivasa Desikan. 2025.

**Supplemental**
- AI Foundations: “Deep Computer Vision Using Convolutional Neural Networks”, “Representation Learning and Generative Learning Using Autoencoders and GANs”, Hands-On Machine Learning with Scikit-Learn, Keras & Tensorflow, chapters 14, 17.
- “Multi-modal Transformers”, Deep Learning: Foundations and Concepts, chapter section 12.4.
- AI Perspectives: “Explainable Deep Learning: Concepts, Methods, and New Developments” by Wojciech Samek in Explainable Deep Learning. 2023.
- AI Designs: “Guiding a Diffusion Model with a Bad Version of Itself.” Karras et al, NeurIPS. 2024.
- “Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction.” 2024. Tian et al. NeurIPS.
- “The Hateful Memes Challenge: Detecting Hate Speech in Multimodal Memes”. 2020.
- Social Designs: “Online images amplify gender bias,” Guilbeault, Douglas, Solène Delecourt, Tasker Hull, Bhargav Srinivasa Desikan, Mark Chu, and Ethan Nadler. Nature. 2024.
- “Sixteen facial expressions occur in similar contexts worldwide” 2020.
- “Using deep learning and Google Street View to estimate the demographic makeup of neighborhoods across the United States” 2017.
- “Computer vision uncovers predictors of physical urban change.” 2017.

**Lab Session:** Avi Oberoi, Tuesday, 11-12am


### Week 9. Mar.6: Alignment, Ethics, Safety, and Novelty

In this final week, we explore the alignment of AI agents to human values, their ethical implications in and for society and safety, and their implications for expanding or contracting the space of ideas and possibilities.

**Required**
- AI Foundations: “Human-Compatible Artificial Intelligence”, Stuart Russell, in Stephen Muggleton and Nick Chater (eds.), Human-Like Machine Intelligence, Oxford University Press, 2021. 
- AI Perspectives: “Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training." Hubinger, E., Denison, C., Mu, J., et al. Anthropic. 2024. 
- “The Alignment Problem from a Deep Learning Perspective.” Ngo, R., Chan, L., & Mindermann, S. ICLR. 2024.
- AI Designs: “Distributional AGI Safety.” Tomasev, N., Franklin, M., Jacobs, J. Krier, S., and Osindero, S. Preprint. 2025.
- “Representation Engineering: A Top-Down Approach to AI Transparency.” Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, … and Dan Hendrycks. 2025.
- Social Perspectives: “We need a new ethics for a world of AI agents.” Gabriel, I., Keeling, G., Manzini, A. and Evans, J., Nature, 644(8075), pp.38-40. 2025.

**Supplemental**
- AI Perspectives: “Carbon-aware computing: Measuring and reducing the carbon intensity associated with software in execution.” Will Buchanan, John Foxon, Daniel Cooke, Sangeeta Iyer, Elizabeth Graham, Bill DeRusha, Christian Binder, Kin Chiu, Laura Corso, Henry Richardson, Vaughan Knight, Asim Hussain, Avi Allison, Nithin Mathews. 2023.
- “All That Glitters is Not Novel: Plagiarism in AI Generated Research”. Tarun Gupta, Danish Pruthi. 2025
- AI Designs: "AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Safety Detection" Weidi Luo, Shenghong Dai, Xiaogeng Liu, Suman Banerjee, Huan Sun, Muhao Chen, Chaowei Xiao. 2025
- “Improve accuracy by adding Automated Reasoning checks in Amazon Bedrock Guardrails. Amazon.” 2025.
- “Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers” Chenglei Si, Diyi Yang, Tatsunori Hashimoto. 2025.
- Social Perspectives: UNESCO AI Ethics framework. 2022.
- “The moral machine experiment.” 2018. Awad, Edmond, Sohan Dsouza, Richard Kim, Jonathan Schulz, Joseph Henrich, Azim Shariff, Jean-François Bonnefon, and Iyad Rahwan. Nature 563, no. 7729: 59-64.
- Social Designs: “Scientific production in the era of large language models.” Keigo Kusumegi, Xinyu Yang, Paul Ginsparg, Mathijs de Vaan, Toby Stuart, and Yian Yin. 2025

**Lab Session:** Gio Choi, Thursday 2-3pm


### Week 10. March. 13: Friday, 1:30-4:20pm, Presentation of Projects via Zoom

**Turn in Final Project due Friday, March 13 by 5pm**
