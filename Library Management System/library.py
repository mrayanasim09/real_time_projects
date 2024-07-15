class Library:

    def __init__(self,name):
        try: 
            with open('books_list.txt', 'r') as f:
                self.l2 = f.read().split('\n')
        except FileNotFoundError:
            print('Error books list file not found')
        
        self.borrowed_books = []
        
        try:
            with open('books_track.txt', 'r') as f:
                self.borrowed_books = f.read().split('  ')
        except FileNotFoundError:
            print('Error books track file not found')

        admin = ['MRayan Asim']

        if name in admin:
            self.admin_main()
        else:
            print(f'Hello {name} welcome to our library')
            self.user_main()

    def user_main(self):
        print('1.Want to borrow a book')
        print('2.Want to return a book')

        try:
            user_choice = int(input('1/2\n'))
        except ValueError:
            print('you entered wrong input try again')
            user_choice = int(input('1/2\n'))
        
        if user_choice == 1:
            self.borrow_book()            

        elif user_choice == 2:
            self.return_book()

        else:
            print('You entered a wrong option')

                
    def admin_main(self):
        print('Welcome admin\n')

        print('1.Add a book')
        print('2.Delete a book')
        print('3.See which books are borrowed')
        print('4.Upade a book')

        try:
            choice = int(input('1/2/3/4\n'))
        except ValueError:
            print('You entered wrong input try again')
            choice = int(input('1/2/3/4\n'))

        if choice == 1:
            self.add_book()
        
        elif choice == 2:
            self.delete_book()

        elif choice == 3:
            self.see_books()
        
        elif choice == 4:
            self.update_book()

        else:
            print('You entered a wrong option')

    def borrow_book(self):
            print('Ok can you tell use which book do you want to borrow?')
            book_name = input('')
            
            with open('books_track.txt','r') as f:
                content = f.read()
                l = content.split('  ')

            if (book_name.lower() in self.l2) and (book_name.lower() not in l):
                print(f'You have borrowed {book_name.lower()} ')

                with open('books_track.txt','a') as f:
                    f.write(f'{book_name.lower()}  ')
            
            elif book_name.lower() not in self.l2 :
                print('Sorry we donot have this book')
            
            elif book_name.lower() in l:
                print('Anyone has already borrowed it please wait')

    def return_book(self):
        print('Ok tell me the name of the book you want to return')
        book_name_return = input('')
            
        with open('books_track.txt','r') as f:
            content = f.read()
            l3 = content.split('  ')
                
        with open('books_track.txt','w') as f:
            if book_name_return in l3:
                new_content = content.replace(book_name_return,'')
                f.write(new_content)
                print('Thank you for returning the book')

            elif book_name_return in content:
                f.write(content)
                print('Please enter full name of the book')

            else:
                f.write(content)
                print('You entered wrong name')

    def add_book(self):
        print('Tell me the book name of the book you want to add in the library')
        book_name = input('')
        self.l2.append(book_name)
        print(f'Now we have these books in library \n')

        for index, item in enumerate(self.l2):
            print(f'{index+1}. {item}')
            
        with open('books_list.txt','a') as f:
            f.write(f'\n{book_name}\n')
    
    def delete_book(self):
        print('Tell me the name of the book you want to add in the library')
        book_name = input('')
        if book_name not in self.l2:
            print('The book is not in our records')

        else:
            self.l2.remove(book_name)
            print(f'Now we have these books in library \n')
            for index,item in enumerate(self.l2):
                print(f'{index+1}. {item}')
                
            with open('books_list.txt','r') as f:
                content = f.read()

            with open('books_list.txt','w') as f:
                new_content = content.replace(book_name,f'\n')
                f.write(new_content)

    def see_books(self):
        with open('books_track.txt','r') as f:
            content = f.read()
            l = content.split('  ')
            for item in l:
                print(item)

            print('These are the books which are borrowed')

    def update_book(self):
        for index, item in enumerate(self.l2):
            print(f'{index+1}. {item}')

        print('Which book name do you want to update? Enter the number of the book:')

        try:
            book_index = int(input('')) - 1
            
            if 0 <= book_index < len(self.l2):
                updated_book = input('Enter the updated name of the book: ').strip()
                self.l2[book_index] = updated_book

                with open('books_list.txt', 'w') as f:
                    f.write('\n'.join(self.l2))
                print('Book name updated successfully')

            else:
                print('Invalid book number')

        except ValueError:
            print('You entered wrong input, try again')

#Example Usage
if __name__== '__main__':
    name = input('Enter your name: ')
    exampele = Library(name)