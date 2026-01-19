from django.core.management.base import BaseCommand
from guides.models import TeamMember


class Command(BaseCommand):
    help = 'Add sample team members to the database'

    def handle(self, *args, **kwargs):
        TeamMember.objects.all().delete()
        
        # Sample team members with placeholder data
        team_members = [
            {
                'name': 'Swostika Acharya',
                'role': 'Lead Trek Guide',
                'bio': 'With over 15 years of experience in the Himalayas, Swostika has led hundreds of successful treks across Nepal and Tibet.',
                'image_url': '',
                'order': 1,
            },
            {
                'name': 'Samikshya',
                'role': 'Senior Guide & Mountaineer',
                'bio': 'Samikshya is a certified mountaineer with expertise in high-altitude treks. She specializes in Annapurna and Everest region expeditions.',
                'image_url': '',
                'order': 2,
            },
        ]
        
        for member_data in team_members:
            TeamMember.objects.create(**member_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully added team member: {member_data["name"]}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'\nTotal team members added: {len(team_members)}')
        )
