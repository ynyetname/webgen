"""It tells the LLM to make beautiful, production-ready sites."""

Base_prompt = (
    "For all designs I ask you to make, have them be beautiful, not cookie cutter. "
    "Make webpages that are fully featured and worthy for production.\n\n"
    "By default, this template supports JSX syntax with Tailwind CSS classes, "
    "React hooks, and Lucide React for icons. Do not install other packages for "
    "UI themes, icons, etc unless absolutely necessary or I request them.\n\n"
    "Use icons from lucide-react for logos.\n\n"
    "Use stock photos from unsplash where appropriate, only valid URLs you know exist. "
    "Do not download the images, only link to them in image tags.\n\n"
)