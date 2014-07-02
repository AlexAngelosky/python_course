import movie

toy_story = movie_archive.Film("Toy Story",
                               "a story about a boy's toys that come to live",
                               "http://www.themoviethemesong.com/wp-content/uploads/2014/04/Toy-Story-Theme-Song-6.jpg",
                               "https://www.youtube.com/watch?v=KYz2wyBy3kc")

the_mask = movie_archive.Film("The mask",
                      "the story of Stanley Ipkiss turning from a looser to a hero by finding a misterious mask in the sea",
                        "http://image.tmdb.org/t/p/original/7plBoAhunhRVVmNCVMVo47Ede53.jpg",
                            "https://www.youtube.com/watch?v=zwGxBZh6gRk")

print(toy_story.storyline)
