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
    st.subheader('Number of Guests Over Time')
    data['booking_date'] = pd.to_datetime(data['booking_date'], unit='ms')
    guests_over_time = data.groupby(data['booking_date'].dt.date).size()
    st.line_chart(guests_over_time)
    st.subheader('Bookings by Distribution Channel')
    distribution_channel_counts = data['distribution_channel'].value_counts()
    st.bar_chart(distribution_channel_counts)
    st.subheader('Bookings by Reservation Status')
    reservation_status_counts = data['reservation_status'].value_counts()
    st.bar_chart(reservation_status_counts)

if __name__ == "__main__":
    main()