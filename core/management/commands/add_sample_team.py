from django.core.management.base import BaseCommand
from core.models import TeamMember


class Command(BaseCommand):
    help = 'Add sample team members (you can customize these)'

    def handle(self, *args, **kwargs):
        team_data = [
            {
                'name': 'Sample Guide 1',
                'role': 'Lead Mountain Guide',
                'bio': 'Replace this with your actual team member bio. Include their experience, certifications, and expertise in Himalayan trekking.',
                'image_url': 'https://via.placeholder.com/400x500/1e40af/ffffff?text=Team+Member+1',
                'order': 1
            },
            {
                'name': 'Sample Guide 2',
                'role': 'Senior Trek Leader',
                'bio': 'Replace this with your actual team member bio. Highlight their knowledge of local culture and mountain safety.',
                'image_url': 'https://via.placeholder.com/400x500/059669/ffffff?text=Team+Member+2',
                'order': 2
            },
            {
                'name': 'Sample Coordinator',
                'role': 'Operations Manager',
                'bio': 'Replace this with your actual team member bio. Describe their role in planning and coordinating successful treks.',
                'image_url': 'https://via.placeholder.com/400x500/ea580c/ffffff?text=Team+Member+3',
                'order': 3
            }
        ]

        for member_data in team_data:
            member, created = TeamMember.objects.get_or_create(
                name=member_data['name'],
                defaults=member_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created team member: {member.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Team member already exists: {member.name}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Sample team members added!'))
        self.stdout.write(self.style.SUCCESS('Visit /team/ to see them'))
        self.stdout.write(self.style.SUCCESS('Edit them in admin panel: /admin/core/teammember/'))
