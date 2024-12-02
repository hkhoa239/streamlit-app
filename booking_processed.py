import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_parquet('booking.parquet')

def main():
    st.title('Booking Data Visualization')
    data = load_data()
    st.write(data)

    st.subheader('Basic Information')
    st.write(f"Number of bookings: {data.shape[0]}")
    st.write(f"Number of unique guests: {data['guest_id'].nunique()}")
    st.write(f"Number of unique hotels: {data['hotel_id'].nunique()}")

    # Convert booking_date to datetime
    data['booking_date'] = pd.to_datetime(data['booking_date'], unit='ms')

    # Number of Guests Over Time
    st.subheader('Number of Guests Over Time')
    guests_over_time = data.groupby(data['booking_date'].dt.date).size()
    st.line_chart(guests_over_time)

    # Bookings by Distribution Channel
    st.subheader('Bookings by Distribution Channel')
    distribution_channel_counts = data['distribution_channel'].value_counts()
    st.bar_chart(distribution_channel_counts)

    # Bookings by Reservation Status
    st.subheader('Bookings by Reservation Status')
    reservation_status_counts = data['reservation_status'].value_counts()
    st.bar_chart(reservation_status_counts)

    # Bookings by Payment Method
    st.subheader('Bookings by Payment Method')
    payment_method_counts = data['payment_method'].value_counts()
    st.bar_chart(payment_method_counts)

    # Average Rating by Hotel
    st.subheader('Average Rating by Hotel')
    avg_rating_by_hotel = data.groupby('hotel_id')['rating'].mean()
    st.bar_chart(avg_rating_by_hotel)

    # Total Amount by Hotel
    st.subheader('Total Amount by Hotel')
    total_amount_by_hotel = data.groupby('hotel_id')['amount'].sum()
    st.bar_chart(total_amount_by_hotel)

    # Average Stay Duration by Hotel
    st.subheader('Average Stay Duration by Hotel')
    avg_stay_duration_by_hotel = data.groupby('hotel_id')['stays_day'].mean()
    st.bar_chart(avg_stay_duration_by_hotel)

    # Bookings by Month
    st.subheader('Bookings by Month')
    data['month'] = data['booking_date'].dt.month
    bookings_by_month = data['month'].value_counts().sort_index()
    st.bar_chart(bookings_by_month)

if __name__ == "__main__":
    main()