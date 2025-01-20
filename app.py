import streamlit as st
from fetch_books import fetch_books
from insert_books import create_connection, insert_book_data

def main():
    st.title("Google Books Data Fetcher")

    search_query = st.text_input("Enter a search term (e.g., 'Python programming'):")

    if st.button("Fetch and Save Data"):
        if not search_query:
            st.error("Please enter a search term.")
            return

        st.info(f"Fetching data for: {search_query}")
        books = fetch_books(search_query)

        if not books:
            st.warning("No books found for this search term.")
            return

        connection = create_connection()

        if connection:
            for item in books:
                volume_info = item.get("volumeInfo", {})
                sale_info = item.get("saleInfo", {})

                book_data = (
                    item.get("id"),
                    search_query,
                    volume_info.get("title"),
                    volume_info.get("subtitle"),
                    ", ".join(volume_info.get("authors", [])),
                    volume_info.get("description"),
                    str(volume_info.get("industryIdentifiers")),
                    volume_info.get("readingModes", {}).get("text", False),
                    volume_info.get("readingModes", {}).get("image", False),
                    volume_info.get("pageCount"),
                    ", ".join(volume_info.get("categories", [])),
                    volume_info.get("language"),
                    volume_info.get("imageLinks", {}).get("thumbnail"),
                    volume_info.get("ratingsCount"),
                    volume_info.get("averageRating"),
                    sale_info.get("country"),
                    sale_info.get("saleability"),
                    sale_info.get("isEbook"),
                    sale_info.get("listPrice", {}).get("amount"),
                    sale_info.get("listPrice", {}).get("currencyCode"),
                    sale_info.get("retailPrice", {}).get("amount"),
                    sale_info.get("retailPrice", {}).get("currencyCode"),
                    sale_info.get("buyLink"),
                    volume_info.get("publishedDate", "")[:4]
                )

                insert_book_data(connection, book_data)

            connection.close()
            st.success("Data fetched and inserted into MySQL successfully!")

if __name__ == "__main__":
    main()
st.title("BOOKSCAPE PROJECT")