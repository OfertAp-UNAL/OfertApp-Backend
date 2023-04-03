from faker import Faker
from auth.models import User, Admin
from publications.models import Publication, Category, Offer, PublicationSupport
from comments.models import Comment, Reaction
from django.core.management.base import BaseCommand
    
class Command(BaseCommand):
    
    help = "Seed elements to database"

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            type=int,
            help='Number of elements to seed'
        )

    def handle(self, *args, **options):
        self.stdout.write("Seeding data")

        number = options.get('number', 10)
            
        fake = Faker(
            ['es_ES']
        )

        usersIds = [ i for i in range(1, number + 1) ]

        # Users seeding
        self.stdout.write("Seeding Users....")
        users = [
            User.objects.create(
                id = i,
                firstName = fake.first_name(),
                lastName = fake.last_name(),
                username = str(i) + fake.user_name(),
                email = str(i) + fake.email(),
                password = fake.password(),
                birthdate = fake.date(),
                address = fake.address(),
                idenIdType = fake.random_element(elements=('CC', 'CE', 'TI', 'PP', 'NIT')),
                phone = str(fake.phone_number()),
                accountType = fake.random_element(elements=('PP', 'EF', 'NQ', 'CD')),
                accountId = i,
                townId = fake.random_element(elements=(
                    1.2, 2.3, 3.4, 4.1, 5.4, 6.2, 7.7, 8.99, 9.10, 10.21
                )),
                verified = True
            )
            for i in usersIds
        ]

        # 10% of Users will be admins        
        _ = [
            Admin.objects.create(
                user = users[i],
                hiredDate = fake.date()
            )
            for i in usersIds[:int(number * 0.1)]
        ]

        self.stdout.write("Seeding Categories (10% of Publications)....")
        
        categories = [
            Category.objects.create(
                name = fake.word()
            )
            for _ in range(int(number * 0.1))
        ]

        self.stdout.write("Seeding Publications....")
        publications = [
            Publication.objects.create(
                title = fake.text(max_nb_chars=45),
                description = fake.text(),
                minOffer = fake.pydecimal(left_digits=13, right_digits=0, positive=True),
                endDate = fake.date_time(),
                available = fake.boolean(),
                reportable = fake.boolean(),
                category = categories[ 
                    fake.random_int(min=0, max=len(categories) - 1)
                ],
                user = users[
                    fake.random_int(min=0, max=len(users) - 1)
                ],
            )
            for _ in range(number)
        ]
        
        self.stdout.write("Seeding Comments.... (10 per Publication)")
        comments = [
            Comment.objects.create(
                text = fake.text(),
                title = fake.text(max_nb_chars=45),
                user = users[
                    fake.random_int(min=0, max=len(users) - 1)
                ],
                publication = publications[
                    i % number
                ],
                parent = None
            )
            for i in range(number*10)
        ]

        # Relate comments with parents randomly
        _ = [
            Comment.objects.filter(id=comments[i].id).update(
                parent = comments[
                    fake.random_int(min=0, max=i)
                ] if fake.boolean() else None
            )
            for i in range(len(comments) - 1, -1, -1)
        ]

        self.stdout.write("Seeding Reactions.... (number * 100)")
        _ = [
            Reaction.objects.create(
                type = fake.random_element(elements=('LIKE', 'DISLIKE', 'WARNING')),
                user = users[
                    fake.random_int(min=0, max=len(users) - 1)
                ],
                comment = comments[
                    fake.random_int(min=0, max=len(comments) - 1)
                ]
            )
            for _ in range(number*100)
        ]

        self.stdout.write("Seeding Offers (10 per Publication)")
        _ = [
            Offer.objects.create(
                amount = fake.pydecimal(left_digits=13, right_digits=0, positive=True),
                user = users[
                    fake.random_int(min=0, max=len(users) - 1)
                ],
                publication = publications[
                    i % number
                ],
                available = fake.boolean()
            )
            for i in range(number*10)
        ]

        self.stdout.write("Seeding PublicationSupports")
        _ = [
            PublicationSupport.objects.create(
                type = 'VIDEO',
                data = "defaultSupport.mp4",
                description = fake.text(),
                publication = publications[
                    fake.random_int(min=0, max=len(publications) - 1)
                ]
            )
            for _ in range(number*10)
        ]