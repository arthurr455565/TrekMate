from django.core.management.base import BaseCommand
from treks.models import Trek


class Command(BaseCommand):
    help = 'Populate database with Annapurna, Everest, and Manaslu treks'

    def handle(self, *args, **kwargs):
        treks_data = [
            {
                'name': 'Annapurna Circuit Trek',
                'location': 'Annapurna Region, Nepal',
                'difficulty': 'Moderate',
                'description': '''The Annapurna Circuit Trek is one of the most popular and diverse trekking routes in Nepal. This classic trek takes you through lush subtropical forests, terraced farmlands, deep gorges, and high mountain passes. 

You'll experience the dramatic landscape changes as you traverse from the lowlands to the high Himalayan desert. The trek offers stunning views of Annapurna, Dhaulagiri, Manaslu, and other peaks over 8,000 meters.

The highlight of the trek is crossing the Thorong La Pass at 5,416 meters, one of the highest trekking passes in the world. Along the way, you'll encounter diverse cultures, from Hindu villages in the lowlands to Tibetan Buddhist communities in the higher elevations.

The trek typically takes 15-20 days and offers a perfect blend of natural beauty, cultural immersion, and physical challenge. You'll visit ancient monasteries, hot springs, and traditional villages while enjoying the hospitality of the local people.''',
                'duration': '15-20 days',
                'altitude': 5416,
                'best_season': 'March-May, September-November',
                'image': 'annapurna trek pic/thorangla-pass.jpg'
            },
            {
                'name': 'Everest Three-Pass Trek',
                'location': 'Everest Region, Nepal',
                'difficulty': 'Hard',
                'description': '''The Everest Three-Pass Trek is the ultimate adventure for experienced trekkers seeking a challenging and rewarding journey through the Khumbu region. This trek combines three high mountain passes - Kongma La (5,535m), Cho La (5,420m), and Renjo La (5,360m) - offering unparalleled views of the world's highest peaks.

This demanding trek takes you through the heart of Sherpa country, visiting iconic locations like Everest Base Camp, Gokyo Lakes, and the famous Khumbu Icefall. You'll witness breathtaking panoramas of Mount Everest, Lhotse, Makalu, Cho Oyu, and countless other Himalayan giants.

The trek offers a unique perspective of the Everest region, taking you off the beaten path to remote valleys and high-altitude lakes. You'll experience the rich Sherpa culture, visit ancient monasteries like Tengboche, and challenge yourself with steep ascents and technical passes.

This 18-21 day adventure requires excellent physical fitness and previous high-altitude trekking experience. The rewards include some of the most spectacular mountain scenery on Earth and a profound sense of accomplishment.''',
                'duration': '18-21 days',
                'altitude': 5535,
                'best_season': 'April-May, September-November',
                'image': 'everest trek pic/IMG_5845.JPG'
            },
            {
                'name': 'Manaslu Circuit Trek',
                'location': 'Manaslu Region, Nepal',
                'difficulty': 'Moderate',
                'description': '''The Manaslu Circuit Trek is a spectacular journey around the world's eighth-highest mountain, Mount Manaslu (8,163m). This trek offers a perfect alternative to the more crowded Annapurna Circuit, providing an authentic and remote Himalayan experience.

The trek takes you through diverse landscapes, from subtropical forests and terraced fields to alpine meadows and high mountain passes. You'll cross the challenging Larkya La Pass at 5,160 meters, which offers stunning panoramic views of Manaslu, Himlung Himal, and other peaks.

This region was only opened to trekkers in 1991, and it still retains its pristine beauty and traditional culture. You'll encounter Tibetan-influenced villages, ancient monasteries, and warm hospitality from the local communities. The trail follows the Budhi Gandaki River through dramatic gorges and past cascading waterfalls.

The Manaslu Circuit typically takes 14-18 days and requires a special restricted area permit. The trek offers a perfect balance of natural beauty, cultural richness, and physical challenge, making it ideal for trekkers seeking an off-the-beaten-path adventure in the Himalayas.''',
                'duration': '14-18 days',
                'altitude': 5160,
                'best_season': 'March-May, September-November',
                'image': 'manaslu trek pic/IMG_5143.JPG'
            }
        ]

        for trek_data in treks_data:
            trek, created = Trek.objects.get_or_create(
                name=trek_data['name'],
                defaults=trek_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created trek: {trek.name}'))
            else:
                # Update existing trek with new image
                for key, value in trek_data.items():
                    setattr(trek, key, value)
                trek.save()
                self.stdout.write(self.style.WARNING(f'Updated trek: {trek.name}'))

        self.stdout.write(self.style.SUCCESS('\nAll treks have been processed!'))
